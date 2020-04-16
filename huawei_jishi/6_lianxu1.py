#!/usr/bin/env python3

while True:
    try:
        n = int(input())
        n2 = bin(n)[2:]
        li = range(len(n2))
        li.reverse()
        for i in li:
            print(i)

    except:
        break
