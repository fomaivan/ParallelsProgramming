#!/usr/bin/python3

import sys

for line in sys.stdin:
    try:
        count, key = line.strip().split('\t', 1)
        count = int(count)

    except ValueError as e:
        continue

    print("{}\t{}".format(key, 9999999 - count))