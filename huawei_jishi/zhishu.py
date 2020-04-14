#!/usr/bin/env python3.7

a = int(input())
def q(x):
    zhi = 1
    for i in range(2,int(x*0.5)):
        if x%i == 0:
            zhi = 0
            print(str(i),end = ' ')
            q(int(x/i))
            break
    if zhi == 1:
        print(str(x),end = ' ')

q(a)

