import sys

if len(sys.argv) < 2:
    print('nog enough arguments')
    exit(1)
elif len(sys.argv) > 3:
    print('too many arguments')
    exit(1)
elif len(sys.argv) < 1:
    print('impossible amount of arguments')
    exit(2)
else:
    print('a nice amount of arguments \U0001F44C')