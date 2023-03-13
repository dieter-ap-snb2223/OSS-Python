r1 = range(4, 16, 3)
r2 = range(2, 9)
r3 = range(10)

for r in (r1, r2, r3):
    print(r)
    for e in r:
        print(e, end=' ')
    print()