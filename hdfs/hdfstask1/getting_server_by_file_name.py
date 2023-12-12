import os
import subprocess
import sys

filepath = sys.argv[1]
command = "hdfs fsck " + filepath + " -files -blocks -locations 2> /dev/null"
full_file_info = os.popen(command).read()

pattern = "DatanodeInfoWithStorage["
ip_info = full_file_info[full_file_info.index(pattern) + len(pattern):]
ip_info = ip_info[:ip_info.index(',')]

if ':' in ip_info:
    ip_info = ip_info[:ip_info.index(':')]

print(ip_info)
