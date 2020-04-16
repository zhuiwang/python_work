#!/usr/bin/env python3

input_count = int(input())

list_word = list()

for i in range(input_count):
    word = input()
    list_word.append(word)

# print(list_word)
sort_list = sorted(list_word)
# print(sort_list)

for i in sort_list:
    print(i)
