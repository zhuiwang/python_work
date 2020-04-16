#!/usr/bin/env python3

def printStr(string):
    if len(string) < 8:
        print(string + '0'*(8 - len(string)))
    else:
        while len(string) > 8:
            print(string[:8])
            string = string[8:]
        print(string + '0'*(8 - len(string)))


a = input()
b = input()

printStr(a)
printStr(b)
