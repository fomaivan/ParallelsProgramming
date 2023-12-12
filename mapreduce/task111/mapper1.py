#!/usr/bin/python3

import sys
import string

for line in sys.stdin:
    try:
        text = line.strip()
    except ValueError as e:
        continue
    words = text.split(' ')
    for word in words:
        word = word.strip().strip(string.punctuation)
        if word != "":
            if word.istitle() and word[1:].islower():
                print("{}\t1\t1".format(word.lower()))
            else:
                print("{}\t0\t1".format(word.lower()))