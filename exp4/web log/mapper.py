#!/usr/bin/python
import sys;
import re;
for line in sys.stdin:
    line = line.strip() 
    words=line.split()
    x=re.findall("http://",words[10])
    if (x):
    	print('%s	%s' %(words[10],1))
