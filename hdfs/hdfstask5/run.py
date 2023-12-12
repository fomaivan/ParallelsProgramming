import re
import sys
import subprocess

filename = "my_awesome_name_for_test_file.txt"
dist_filename = "/tmp/" + filename

def get_block_path(block_id):
    block_pattern = r"Block replica.+:\s(.+)\/"
    block_cmd = ["hdfs", "fsck", "-blockId", block_id]

    block_output = subprocess.check_output(block_cmd).decode("utf-8")
    nodename = re.search(block_pattern, block_output).group(1)

    node_cmd = ["ssh", "hdfsuser@" + nodename, "find", "/dfs", "-name", block_id]
    node_output = subprocess.check_output(node_cmd).decode("utf-8").rstrip()
    return nodename, node_output


subprocess.check_output(["dd", "if=/dev/zero", "of=" + filename, "bs=" + sys.argv[1], "count=1"])
subprocess.check_output(["hdfs", "dfs", "-put", filename, dist_filename])

raw_blocks_output = subprocess.check_output(["hdfs", "fsck", dist_filename, "-files", "-blocks", "-locations"])
block_ids = re.findall(r':(blk_[0-9]+)_[0-9]+', raw_blocks_output.decode("utf-8"))

memory = 0
for block_id in block_ids:
    node, path = get_block_path(block_id)
    raw_size = subprocess.check_output(["ssh", "hdfsuser@" + node, "wc", "-c", path])
    memory += int(raw_size.split()[0])

subprocess.check_output(["rm", filename])
subprocess.check_output(["hdfs", "dfs", "-rm", "-skipTrash", dist_filename])
print(memory - int(sys.argv[1]))

