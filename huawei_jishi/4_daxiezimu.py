#!/usr/bin/env python3


while True:
    try:
        string = input()
        num = 0
        for s in string:
            if 'A' <= s <= 'Z':
                num += 1
        print(num)
    except:
        break

