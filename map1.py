#!/usr/bin/env python
  
import sys
#import pandas as pd

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    words = line.split(',')
    # increase counters
    if len(words[1])>5 or len(words[13])<1 or len(words[14])<1 or len(words[15])<1:#get rid of first line and NA
        print '%s\t%s' % (words[1], 0)
    elif float(words[13])>15.00 or float(words[14]) >15.00 or float(words[15]) >0.00:#if too late or cancelled
        print '%s\t%s' % (words[1], 1)#late
    else:
        print '%s\t%s' % (words[1], -1)#ontime (include CANCELED)

#    for word in words:
 #       if row[1]['DEP_DELAY_NEW'] >15 or row[1]['ARR_DELAY_NEW'] >15:
  #      print(row[1]['OP_UNIQUE_CARRIER'], 1)


#a = pd.read_csv(sys.stdin, delimiter = ',')

#for row in a.iterrows():
 #   if row[1]['DEP_DELAY_NEW'] >15 or row[1]['ARR_DELAY_NEW'] >15:
  #      print(row[1]['OP_UNIQUE_CARRIER'], 1)
