#!/usr/bin/env python3

def fun1(s):
    if len(s) > 8:
        return True
    else:
        return False

def fun2(s):
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    for ss in s:
        if 'a'<=ss<='z':
            num1 = 1
        elif 'A' <=ss<='Z':
            num2 = 1
        elif '0'<=ss<='9':
            num3 = 1
        else:
            num4 = 1

    if (num1+num2+num3+num4) >= 3:
        return True
    else:
        return False

def fun3(s):
    for i in range(len(s)-3):
        if s[i:i+3] in s[i+1:]:
            return False
            break
    return True

while True:
    try:
        a = input()
        if fun1(a) and fun2(a) and fun3(a):
            print('OK')
        else:
            print('NG')

    except:
        break
