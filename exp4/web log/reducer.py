#!/usr/bin/python
import sys;
from operator import itemgetter;
prev_word = None
prev_count = 0
word = None
for line in sys.stdin:
	line = line.strip()
	word,count = line.split('\t',1)
	count=int(count)
	if word == prev_word:
		prev_count+=1;
	else:
		if prev_word:
			print('%s	%s' %(prev_word,prev_count))
		prev_word = word;
		prev_count = count;
print('%s	%s' %(prev_word,prev_count))
