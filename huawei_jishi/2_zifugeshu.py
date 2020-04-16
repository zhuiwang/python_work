#!/usr/bin/env python3

string = input()
find = input()
times = 0

for i in range(len(string)):
    if find.lower() == string[i].lower:
        times = times + 1

print(times)
