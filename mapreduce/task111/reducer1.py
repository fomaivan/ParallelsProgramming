#!/usr/bin/python3

import sys

current_key = None

title_sum_count = 0
sum_count = 0

for line in sys.stdin:
    try:
        key, title_count, count = line.strip().split('\t', 2)

        title_count = int(title_count)
        count = int(count)

    except ValueError as e:
        continue

    if current_key != key:
        if current_key and title_sum_count == sum_count:
            print("{}\t{}".format(current_key, sum_count))

        sum_count = title_sum_count = 0
        current_key = key

    sum_count += count
    title_sum_count += title_count

if current_key and title_sum_count == sum_count:
    print("{}\t{}".format(current_key, sum_count))