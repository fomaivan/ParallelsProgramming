#!/usr/bin/python3

import sys
import random

for line in sys.stdin:
    try:
        index = line.strip()
    except ValueError as e:
        continue

    random_num = random.randint(0, 10**20)
    add_index_on_line = random.randint(1, 5)

    #print(f"{random_num}\t{index}\t{add_index_on_line}")
    print("{}\t{}\t{}".format(random_num, index, add_index_on_line))
