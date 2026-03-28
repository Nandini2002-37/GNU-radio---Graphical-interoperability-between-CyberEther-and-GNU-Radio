#!/usr/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/nandini/gsoc/gr-cyberether/python/cyberether
export GR_CONF_CONTROLPORT_ON=False
export PATH="/home/nandini/gsoc/gr-cyberether/build/python/cyberether":"$PATH"
export LD_LIBRARY_PATH="":$LD_LIBRARY_PATH
export PYTHONPATH=/home/nandini/gsoc/gr-cyberether/build/test_modules:$PYTHONPATH
/usr/bin/python3 /home/nandini/gsoc/gr-cyberether/python/cyberether/qa_freqsink.py 
