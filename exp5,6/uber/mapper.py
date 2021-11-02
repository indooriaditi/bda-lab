#!/usr/bin/python3

import sys;
import re;
for line in sys.stdin:
	line = line.strip()
	words=line.split(',')
	model = words[0]
	count = words[3]
	try:
		count = int(count)
	except ValueError:
		continue
	print('%s\t%s'%(model,count))