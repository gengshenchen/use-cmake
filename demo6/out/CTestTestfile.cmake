# CMake generated Testfile for 
# Source directory: /home/ubuntu/work/cmake/demo6
# Build directory: /home/ubuntu/work/cmake/demo6/out
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test([=[test_usage]=] "demo")
set_tests_properties([=[test_usage]=] PROPERTIES  PASS_REGULAR_EXPRESSION "Usage: .* base exponent" _BACKTRACE_TRIPLES "/home/ubuntu/work/cmake/demo6/CMakeLists.txt;82;add_test;/home/ubuntu/work/cmake/demo6/CMakeLists.txt;0;")
add_test([=[test_5_2]=] "demo" "5" "2")
set_tests_properties([=[test_5_2]=] PROPERTIES  PASS_REGULAR_EXPRESSION "is 25" _BACKTRACE_TRIPLES "/home/ubuntu/work/cmake/demo6/CMakeLists.txt;87;add_test;/home/ubuntu/work/cmake/demo6/CMakeLists.txt;93;do_test;/home/ubuntu/work/cmake/demo6/CMakeLists.txt;0;")
add_test([=[test_10_5]=] "demo" "10" "5")
set_tests_properties([=[test_10_5]=] PROPERTIES  PASS_REGULAR_EXPRESSION "is 100000" _BACKTRACE_TRIPLES "/home/ubuntu/work/cmake/demo6/CMakeLists.txt;87;add_test;/home/ubuntu/work/cmake/demo6/CMakeLists.txt;94;do_test;/home/ubuntu/work/cmake/demo6/CMakeLists.txt;0;")
subdirs("math")
