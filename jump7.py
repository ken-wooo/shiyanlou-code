#!/usr/bin/python3

for i in range(1, 101):
    if i % 7 == 0:
        continue
    a = str(i).zfill(2)
    if int(a[0]) == 7 or int(a[1]) == 7:
        continue
    print (i)
