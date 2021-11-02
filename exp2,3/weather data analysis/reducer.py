#!/usr/bin/python
import sys
dmax=dict()
y_list=list()
dmin=dict()
for line in sys.stdin:
    line = line.strip()
    year,temp = map(int,line.split())
    if year not in y_list:
        y_list.append(year)
        dmax[year]=temp
        dmin[year]=temp
    else:
        if dmax[year]<temp:
            dmax[year]=temp
        if dmin[year]>temp:
            dmin[year]=temp
print('--------------------------------')
print('year max_temp min_temp')
print('--------------------------------')
for i in dmax.keys():
    print('%s----------%s-----------%s' %(i,dmax[i],dmin[i]))
