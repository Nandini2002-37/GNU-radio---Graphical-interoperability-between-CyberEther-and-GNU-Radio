#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.9.2

from gnuradio import analog
from gnuradio import cyberether
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation

import superluminal as lm
import time
from dataclasses import dataclass


@dataclass
class SignalState:
    variable_cyberether_slider_0 = [5.0]

state = SignalState()

class test(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.variable_cyberether_slider_0 = variable_cyberether_slider_0 = 5
        
        
        lm.box(
            "Controls",
            [[1, 0, 0], [1, 0, 0]],
            lambda: [
                 lm.slider("Frequency (Hz)", 1, 10, state.variable_cyberether_slider_0)
            ],
        )

        ##################################################
        # Blocks
        ##################################################

        self.cyberether_freqsink_0 = cyberether.time_sink(samp_rate=samp_rate)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, variable_cyberether_slider_0, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.cyberether_freqsink_0, 0))

    def update_cyberether_variables(self):
        if not self.variable_cyberether_slider_0 == state.variable_cyberether_slider_0[0]:
            self.variable_cyberether_slider_0 = variable_cyberether_slider_0 = state.variable_cyberether_slider_0[0]
            self.analog_sig_source_x_0.set_frequency(self.variable_cyberether_slider_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)




def main(top_block_cls=test, options=None):

    tb = top_block_cls()
    tb.start()

    def callback():
        while lm.running():
            tb.cyberether_freqsink_0.update_graph()
            tb.update_cyberether_variables()
            time.sleep(0.01)

    lm.realtime(callback)

if __name__ == '__main__':
    main()
