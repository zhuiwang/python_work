#!/usr/bin/env python3.5
while True:
    try:
        total_number = int(input())

        myset = set()

        for number in range(total_number):
            myset.add(input())

        for number in sorted(myset):
            print(number)
    except:
        break
