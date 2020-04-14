#!/usr/bin/env python3.5

total_number = 11
number_set = [10,20,40,32,67,40,20,89,300,400,15]

mylist=set()
print("start")
for i in range(total_number):
    mylist.add(number_set[i])

print(sorted(mylist))

