#!/usr/bin/env python3.5

total = int(input())
a = dict()
for i in range(total):
    key_value = input().split()
    if key_value[0] in a.keys():
        a[key_value[0]] = a[key_value[0]] + int(key_value[1])
    else:
        a[key_value[0]] = int(key_value[1])

s = list()

for i in a.keys():
    s.append(int(i))

for i in sorted(s):
    print(i, a[str(i)], sep=' ')
