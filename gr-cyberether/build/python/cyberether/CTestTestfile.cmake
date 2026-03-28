# CMake generated Testfile for 
# Source directory: /home/nandini/gsoc/gr-cyberether/python/cyberether
# Build directory: /home/nandini/gsoc/gr-cyberether/build/python/cyberether
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(qa_freqsink "/usr/bin/sh" "qa_freqsink_test.sh")
set_tests_properties(qa_freqsink PROPERTIES  _BACKTRACE_TRIPLES "/usr/lib/x86_64-linux-gnu/cmake/gnuradio/GrTest.cmake;119;add_test;/home/nandini/gsoc/gr-cyberether/python/cyberether/CMakeLists.txt;39;GR_ADD_TEST;/home/nandini/gsoc/gr-cyberether/python/cyberether/CMakeLists.txt;0;")
subdirs("bindings")
