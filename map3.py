#!/usr/bin/env python
  
import sys

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    words = line.split(',')
    # increase counters
    if len(words[16]) >2:
        print '%s\t%s' % (words[16], 1)
