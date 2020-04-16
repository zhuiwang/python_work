#!/usr/bin/env python3

number = input()

list_number = list(number)[::-1]

# print(list_number)

new_list = list()

for i in list_number:
    if i in new_list:
        continue
    else:
        new_list.append(i)

# print(new_list)

num = 0
e = 1
for i in new_list[::-1]:
    num = num + int(i)*e
    e = e*10

print(num)
