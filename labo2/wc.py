#!/usr/bin/python3

fd = open('test.py', 'r')
data = fd.read()
fd.close()
numchars = len(data)
numwords = len(data.split())
numlines = len(data.split('\n'))
print(numlines, numwords, numchars, 'test.py')