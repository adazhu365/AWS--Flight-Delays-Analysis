#!/usr/bin/env python
  
import sys

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    words = line.split(',')
    # increase counters
    #if len(words[1])>5 or len(words[14])<1:#get rid of first line and NA
     #print '%s\t%s' % (words[1], 0)
    if words[1] == '"OH"'and len(words[14]) >0:
    #elif float(words[13])>15.00 or float(words[14]) >15.00 or float(words[15]) >0.00:#if too late or cancelled
        print '%s\t%s' % (words[1]+words[4]+words[9], words[14])#late

    elif words[1] == '"B6"'and len(words[14]) >0:

        print '%s\t%s' % (words[1]+words[4]+words[9], words[14])
        #elif float(words[13])>15.00 or float(words[14]) >15.00 or float(words[15]) >0.00:#if too late or cancelled

    elif words[1] == '"F9"'and len(words[14]) >0:
        print '%s\t%s' % (words[1]+words[4]+words[9], words[14])
    #elif float(words[13])>15.00 or float(words[14]) >15.00 or float(words[15]) >0.00:#if too late or cancelled

    #else:

     #print '%s\t%s' % (words[1], -1)#ontime (include CANCELED)
