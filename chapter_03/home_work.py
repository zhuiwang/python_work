#!/usr/bin/env python3
def devide(homework):
    print('')
    print('-------------------------------------------------------------------')
    print('|                           unit [' + homework + ']                             |')
    print('-------------------------------------------------------------------')
    print('')

# 3-1 姓名
devide('3-1')
name_list = ['zhao', 'qian', 'sun', 'li']
print(name_list)
for name in name_list:
    print(name)

# 3-2 问候语
devide('3-2')
hello = 'Good morning'
for name in name_list:
    print(hello + ' ' + name)

# 3-3 自己的列表
devide('3-3')
ways = ['run', 'work', 'bicycle', 'bus', 'tx']
for way in ways:
    print('I would like to own a Honada '+ way)

'''
append() insert() del() 
pop() 返回删除的值内容
remove() 只删除列表中的第一个指定的元素，如果全部删除需要循环
'''
# 3-4 嘉宾名单
devide('3-4')
invite_list = ['qunzhu', 'aman', 'wenyuanwa']
for invite_person in invite_list:
    print('Hi %s would i invite you to have a dinner ?' % invite_person.title())

# 3-5 修改嘉宾名单
devide('3-5')
print('Howerver %s could not have this invite' % invite_list[0].title())
invite_list.remove('qunzhu')
print(invite_list)
invite_list.append('someone')
print(invite_list)
invite_list.insert(0, 'jackma')
print(invite_list)
for invite_person in invite_list:
    print('Hi %s would i invite you to have a dinner ?' % invite_person.title())

# 3-6 添加嘉宾
devide('3-6')
print('I found a bigger dining table.')
invite_list.insert(3, 'zhoujielun')
invite_list.append('caixukun')
print(invite_list)
for invite_person in invite_list:
    print('Hi %s would i invite you to have a dinner ?' % invite_person.title())

# 3-7 缩减名单
devide('3-7')
print('I only have to del to two person')
for i in range(2):
    del_pop = invite_list.pop()
    print(del_pop)

for invite_person in invite_list:
    print('Hi %s would i invite you to have a dinner ?' % invite_person.title())

print(invite_list)
for personal in invite_list:
    print(personal)
    invite_list.remove(personal)

print(invite_list)

list_test = ['a', 'b', 'c', 'd', 'e','f']
for test in list_test:
    list_test.remove(test)
    print(list_test)


'''
sort() 
sorted()
reverse()
len(cars)

'''
# 3-8 放眼世界
devide('3-8')
wanner_to_go = ['unit status', 'paris', 'universal', 'niagara Falls']
for place in wanner_to_go:
    print(place)
place_sorted = sorted(wanner_to_go)
print('------ after sorted ------')
for place in place_sorted:
    print(place)

print('------ sorted(wanner_to_go) ------')
for place in sorted(wanner_to_go):
    print(place)

print('------ reverse(wanner_to_go) ------')
for place in reversed(wanner_to_go):
    print(place)

print(wanner_to_go)
sort_place = wanner_to_go.sort()
print(wanner_to_go)
print(sort_place)


people_number = len(wanner_to_go)
print(people_number)

motorcycles = ['unite']
print(motorcycles[-1])



