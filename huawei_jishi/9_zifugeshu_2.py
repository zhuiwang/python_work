#!/usr/bin/env python3
inputString = input()
count = 0
stringArr = []
for i in range(len(inputString)):
    if inputString[i] not in stringArr:
        stringArr.append(inputString[i])
for i in range(len(stringArr)):
    if int(ord(stringArr[i])) < 127 and int(ord(stringArr[i]) > 0):
        count = count + 1
print(count)
