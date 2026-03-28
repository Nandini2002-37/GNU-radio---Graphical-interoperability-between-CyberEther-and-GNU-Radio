#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2026 nandini.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr
import superluminal as lm
from collections import deque 
import time

class freqsink(gr.sync_block):
    """
    docstring for block freqsink
    """
    def __init__(self,samp_rate):
        gr.sync_block.__init__(self,
            name="freqsink",
            in_sig=[np.complex64, ],
            out_sig=None)

        self.data_i = np.zeros((1, int(samp_rate*2)), dtype = np.float32)
        self.data = np.zeros((1, int(samp_rate*2)), dtype = np.float32)

        
        lm.plot(
            self.data_i,
            lm.line,
            label="Sine",
            #domain=(lm.time, lm.frequency),
        )

        self.phase = 0
        self.q = deque(maxlen=500) 
        self.last_update = time.perf_counter()
        
    def work(self, input_items, output_items):
        in0 = input_items[0]
        
        n = len(in0)  # could be 4095, 4096, or any size

        # shift old data to the left
        self.data[0, :-n] = self.data[0, n:]
        self.data[0, -n:] = in0.real

        return len(input_items[0])


    def update_graph(self, trigger_level=0.3, pre_samples=0,edge=0):

        # check time interval
        now = time.perf_counter()
        if now - self.last_update < 0.1:
            return
        
        self.last_update = now
        self.dnw =  self.data.copy()

        # 1. Find first rising-edge trigger crossing
        crossings = np.where((self.dnw[0] <= trigger_level+0.01) & (self.dnw[0] >= trigger_level-0.01))[0]

        if len(crossings) == 0:
            # no trigger found, just plot latest buffer
            trigger_idx = 0
        else:
            valid = crossings + 5 < len(self.dnw[0])
            crossings_valid = crossings[valid]

            # compute edge_detect
            edge_detect = self.dnw[0][crossings_valid + 5] - self.dnw[0][crossings_valid]

            # find first positive value
            positive_indices = np.where(edge_detect > 0)[0]

            if len(positive_indices) > 0:
                first_pos_idx = positive_indices[0]         # index in edge_detect array
                crossing_idx = crossings_valid[first_pos_idx]  # corresponding index in original data

            trigger_idx = crossing_idx

        # 2. Adjust start index for pre-trigger samples
        start = max(trigger_idx - pre_samples, 0)
        end = start + self.dnw.shape[1]

        # 3. Slice buffer for display
        if end > self.dnw.shape[1]:
            # not enough samples at the end, wrap with np.roll
            self.data_i[0,:] = np.roll(self.dnw[0], -start)[:self.dnw.shape[1]]
        else:
            self.data_i[0,:] = self.dnw[0, start:end]

        # 4. Update the plot
        lm.update()