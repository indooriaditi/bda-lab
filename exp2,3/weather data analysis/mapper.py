#!/usr/bin/python
import sys
l=list()
for line in sys.stdin:
    line = line.strip()
    year=int(line[15:19])
    temp=int(line[87:92])
    l.append([year,temp])
for record in l:
    print('%s %s' %(record[0],record[1]))
