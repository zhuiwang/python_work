#!/usr/bin/env python3

input_number = int(input(),10)
bin_input = bin(input_number)[2:]
# print(bin_input)
list_input_number = list(bin_input)

count = 0
for i in list_input_number:
    if i == '1':
        count +=1

print(count)
