# python_work
'''
20 9 24
10 2 4 3 5 10 2 18 9 7 2 2 1 3 12 1 8 6 2 2
00 4 01 02 03 04
02 1 05
04 2 06 07
03 3 11 12 13
06 1 09
07 2 08 10
16 1 15
13 3 14 16 17
17 2 18 19
'''
'''
10 5 2 7
10 4 10
10 3 3 6 2 
10 3 3 6 2
'''

def read_input():
    node_num, non_leaf_node_num, target_capacity = map(int, input().split(" "))
    node_capacity = map(int, input().split(" "))

    node_relations = list()

    non_leaf_node_num_temp = non_leaf_node_num
    while non_leaf_node_num_temp:
        all_info = list(map(int, input().strip().split(" ")))
        __id = all_info[0]
        __childs = all_info[2:]
        __info = {'id': __id, 'childs': __childs}
        node_relations.append(__info)
        non_leaf_node_num_temp -= 1

    return node_num, non_leaf_node_num, target_capacity, node_capacity, node_relations


def func():
    node_num, non_leaf_node_num, target_capacity, node_capacity, node_relations = read_input()

    # please finish the function body here.

    # please define the python3 output here. For example: print().


if __name__ == "__main__":
    func()
