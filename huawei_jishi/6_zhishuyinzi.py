#!/usr/bin/env python3


a = int(input())
zhi_list = list()

def q(x):
    zhi = 1
    for i in range(2, int(x*0.5)):
        if x%i == 0:
            zhi = 0
            zhi_list.append(i)
            q(int(x/i))
            break

    if zhi == 1:
        zhi_list.append(x)
        str_zhi_list = [str(x) for x in zhi_list]
        print(' '.join(str_zhi_list))
q(a)
