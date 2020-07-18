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
···
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
···

···
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


def find(node_id, node_capacity_list, node_relations_dict, target_capacity, path, path_result):
    path.append(node_capacity_list[node_id])
    new_path_result = path_result
    if not node_relations_dict.get(node_id) and sum(path) is target_capacity:
        new_path_result.append(path.copy())
    elif not node_relations_dict.get(node_id):
        pass
    else:
        for child_id in node_relations_dict.get(node_id):
            new_path_result = find(child_id, node_capacity_list, node_relations_dict, target_capacity, path, path_result)
    path.pop()
    return new_path_result


def func():
    node_num, non_leaf_node_num, target_capacity, node_capacity, node_relations = read_input()
    node_capacity_list = []
    for capacity in node_capacity:
        node_capacity_list.append(capacity)

    node_relations_dict = {}
    for relation in node_relations:
        node_relations_dict[relation.get("id")] = relation.get("childs")

    path_result = find(0, node_capacity_list, node_relations_dict, target_capacity, [], [])
    path_result.sort(reverse=True)

    for item in path_result:
        line_string = ""
        for sub_item in item:
            line_string += str(sub_item) + " "
        print(line_string[:-1])


if __name__ == "__main__":
    func()
···
