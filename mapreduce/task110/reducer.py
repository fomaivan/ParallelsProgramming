#!/usr/bin/python3

import sys

curr_counter = -1
upper_counter = 0

curr_index_list = []

for line in sys.stdin:
    try:
        random_num, index, add_index_on_line = line.strip().split('\t', 2)

        random_num = int(random_num)
        add_index_on_line = int(add_index_on_line)
    except ValueError as e:
        continue

    curr_index_list.append(index)

    if curr_counter < upper_counter:    
        curr_counter += 1
    else:
        print(','.join(curr_index_list))
        curr_index_list = []
        upper_counter = random_num % 5
        curr_counter = 0