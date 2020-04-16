#!/usr/bin/env python3

while True:
    try:
        a = int(input())
        jihe = set()
        for i in range(a):
            jihe.add(int(input()))
        for i in sorted(jihe):
            print(i)

    except:
        break
