#!/usr/bin/env python
  
from operator import itemgetter
import sys

current_word = None
current_count = 0.00
total = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = float(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count

        total +=1
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s' % (current_word, float(current_count)/total)
        current_count = count
        current_word = word
        total = 1

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s' % (current_word, float(current_count)/total)
