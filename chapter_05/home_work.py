#!/usr/bin/env python3
def devide(homework):
    print('')
    print('-------------------------------------------------------------------')
    print('|                           unit [' + homework + ']                             |')
    print('-------------------------------------------------------------------')
    print('')

# 5-1 条件测试
devide('5-1')
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 5-2
devide('5-2')

string_one = 'strings'
string_two = 'strings'
string_three = 'string'
string_four = 'STRINGS'
print(string_one == string_two)
print(string_one == string_three)
print(string_four == string_one.upper())

name_list = ['name1', 'name2', 'name3']
if 'name1' in name_list:
    print('name1 in name list')
if 'name4' in name_list:
    print('name4 in name list')
else:
    print('name4 not in name list')

# 5-3
devide('5-3')

alien_color_list = ['green', 'yello', 'red']
alien_color = 'green'
if alien_color == 'green':
    print('player get five points')



# 5-6
devide('5-6')
age = 10

if age < 2:
    print('yinger')
elif age < 4:
    print('xuebu')
elif age < 13:
    print('ertong')

# 5-7
devide('5-7')
favorate_fruit_list = ['apple', 'banana', 'pairs']
if 'banana' in favorate_fruit_list:
    print('You really like banana')

# 5-8
devide('5-8')
user_list = ['admin', 'userone', 'user_two', 'user_three']
for user in user_list:
    if user == 'admin':
        print('Hello ' + user + ', would you like to see a status report?')
    else:
        print('Hello ' + user + ', thank you for logging in again')

# 5-9
devide('5-9')
users = []
if users:
    for user in users:
        print('Hello ' + user + ', would you like to see a status report?')
    else:
        print('Hello ' + user + ', thank you for logging in again')
else:
    print('We need to find some users!')

# 5-10 检查用户名
devide('5-10')
currrent_users = ['Rusa', 'Eric', 'Luohan', 'Mous', 'Ning']
new_users = ['eric', 'Luohan', 'Jackylove', 'Jiao', 'TheShy']
currrent_users_lower = [user.lower() for user in currrent_users]
for user in new_users:
    if user.lower() in currrent_users_lower:
        print(user + ' has already in current user list')
    else:
        print(user + ' has not been used')

# 5-11 序数
devide('5-11')

numbers = list(range(1,10))
print(numbers)
for number in numbers:
    if number == 1:
        print(str(number)+'st')
    elif number == 2:
        print(str(number)+'nd')
    elif number == 3:
        print(str(number)+'rd')
    else:
        print(str(number)+'th')



