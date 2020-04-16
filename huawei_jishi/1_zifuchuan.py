#!/bin/env python3

while True:
    try:
        str1 = input()
        str2 = input()
        cnt = 0
        for i in str1:
            if i in str2:
                cnt += 1
        if cnt == len(str1):
            print('true')
        else:
            print('false')
    except:
        break
