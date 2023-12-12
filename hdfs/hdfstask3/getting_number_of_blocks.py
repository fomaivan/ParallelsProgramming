import os
import sys

filepath = sys.argv[1]
command = "hdfs fsck " + filepath + " -blocks 2> /dev/null | grep Total\ blocks"
info = os.popen(command).read()

number_of_blocks = info.split()[3]
print(number_of_blocks)
