#!/usr/bin/env python3

import sys
check = ['A', 'D', 'W', 'S']
check_2 = ['0','1','2','3','4','5','6','7','8','9']
move_point = list()

def leagl_int_numbers(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True

while True:
    try:
        text = sys.stdin.readline().split(';')
        # print(text)
        initx = 0
        inity = 0
        new_text = [x for x in text if x!='']
        # print(new_text)
        for i in new_text:
            # print(i)
            #print(i[1:])
            if i[0] in check:
                if leagl_int_numbers(i[1:]):
                    move_point.append(i)
                    # print(move_point)
                else:
                    continue

        for i in move_point:
            # print(i)
            if i[0] == 'A':
                initx = initx - int(i[1:])

            if i[0] == 'S':
                inity = inity - int(i[1:])

            if i[0] == 'W':
                inity = inity + int(i[1:])

            if i[0] == 'D':
                initx = initx + int(i[1:])

        print('{0},{1}'.format(initx,inity))
            # print("%d,%d"(initx,inity))
        # print("%d,%d"(initx,inity))

    except:
        break
