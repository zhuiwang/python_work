#!/usr/bin/env python3

import string
a = input()

list_a = list(a)
new_list_a = list()
# print(list_a)
count = 0
for i in range(len(a)):
    if a[i] not in new_list_a:
        new_list_a.append(a[i])

for i in new_list_a:
    if i in string.ascii_letters:
        if 0<int(ord(i))<127:
            count += 1

print(count)
