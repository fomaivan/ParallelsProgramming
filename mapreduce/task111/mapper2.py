#!/usr/bin/python3

import sys

for line in sys.stdin:
    try:
        key, count = line.strip().split('\t', 1)
        count = int(count)

    except ValueError as e:
        continue

    if 6 <= len(key) <= 9:
        print("{}\t{}".format(9999999 - count, key))