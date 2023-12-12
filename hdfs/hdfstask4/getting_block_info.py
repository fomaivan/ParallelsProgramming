import os
import sys

block_id = sys.argv[1]

# getting name of server
command = "hdfs fsck -blockId " + block_id + ' 2> /dev/null | grep -m1 "Block replica on" 2> /dev/null'
server_name = os.popen(command).read()
server_name = server_name[server_name.index(':') + 2:]
server_name = server_name[:server_name.index(' ')]
if '/' in server_name:
    server_name = server_name[:server_name.index('/')]

# checking errors
if len(server_name) == 0:
    # Error: block doesn't exist
    print("Error: block doesn't exist\n")
    sys.exit(0)

# getting path to block from root
command = 'ssh hdfsuser@mipt-node01.atp-fivt.org find /dfs -name "' + block_id + '" 2> /dev/null'
block_path = os.popen(command).read()
if '\n' in block_path:
    block_path = block_path[:block_path.index('\n')]

print(server_name + ':' + block_path)
