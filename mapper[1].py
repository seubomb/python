#!/usr/bin/python

import sys

is_first_line=True
for line in sys.stdin:
    if is_first_line:
       is_first_line=False
       continue
    row=line.split(',')
    open_price=float(row[1])
    close_price=float(row[-3])
    change=(open_price-close_price)/open_price*100
    change_text=str(round(change,1))+"%"
    print "%s\t%d" % (change_text,1)

