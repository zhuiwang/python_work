#!/usr/bin/env python3


import sys

error_list = list()
error_times = list()

while True:
    error_log = sys.stdin.readline().strip()
    if error_log == '':
        break

    error_tree = error_log.split(' ')[0]
    error_line = error_log.split(' ')[1]
    # print(error_log)
    # print(error_tree)
    # print(error_line)

    error_file = error_tree.split('\\')[-1]
    # print(error_file)
    # print(len(error_file))
    if len(error_file) > 16:
        error_file = error_file[-16:]
    # print(error_file)

    error = (error_file +' '+ error_line)
    # print(error)
    if error not in error_list:
        error_list.append(error)
        error_times.append(1)
    else:
        if error in error_list:
            index_num =  error_list.index(error)
            # print(index_num)
            error_times[index_num] += 1
            # print(error_times)
    # else:
        # num = error_file_list.index(error_file)
        # if

for i in range(len(error_list)):
    print("%s %s"%(error_list[i], error_times[i]))
