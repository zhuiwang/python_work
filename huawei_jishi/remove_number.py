#!/usr/bin/env python3.5

while True:
    try:
        number = int(input())
        myset = set()
        print(myset)
        for i in range(number):
            myset.add(int(input()))

        for i in sorted(myset):
            print(i)
        print(myset)
    except:
        break
