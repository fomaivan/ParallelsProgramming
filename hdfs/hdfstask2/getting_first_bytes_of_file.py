import sys
from hdfs import Config

filepath = sys.argv[1]
number_of_bytes = 10

client = Config('./.hdfscli.cfg').get_client()
with client.read(filepath, encoding='utf-8') as reader:
    data = reader.read(number_of_bytes)

print(data)
