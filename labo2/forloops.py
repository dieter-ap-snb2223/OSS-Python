import sys

ff = open(sys.argv[1], 'r')
for line in ff:
    print(line, end='')
ff.close()