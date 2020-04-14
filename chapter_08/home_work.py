#!/usr/bin/env python3


def devide(homework):
    print('')
    print('-------------------------------------------------------------------')
    print('|                           unit [' + homework + ']                             |')
    print('-------------------------------------------------------------------')
    print('')

# message
devide('8-1')

def desplay_message():
    print("I have learn function in this chapter")

desplay_message()

devide('8-2')
def favorite_book(title):
    print('One of my favorite books is ' + title)

favorite_book('Alice in Wonderland')

# 8-3 T shirt

devide('8-3')
def make_shirt():
    print('I')


devide('8-5')
def describe_city(name, country):

    print(name + ' is in ' + country)

describe_city('vdaq', 'da')
describe_city('sadew', 'dsa')

# 8-7
devide('8-7')
album_dic = {}
def make_album(singer, album):
    album_dic[singer] = album
    print(album_dic)

make_album('singers', 'xsa')
make_album('singer', 'xsa')
make_album('singe', 'xsa')
make_album('sing', 'xsa')
make_album('sin', 'xsa')

# 8-9
devide('8-9')
magicians = ['liuqian', 'liubiao', 'zhangfei']

def show_list(list):
    for item in list:
        print(item)

show_list(magicians)

# 8-10
def make_great(list):
    new_list= []
    for item in list:
        new_list.append("the Great " + item)

    return new_list

print(make_great(magicians))

def make_great_2(names):
    while names:
        great_name = 'the Great ' + names.pop()
        new_names.append(great_name)
    return new_names

new_names = []
new_names = make_great_2(magicians[:])
print(new_names)

# 8-12
devide('8-12')
def make_sandwich(*addings):
    for add in addings:
        print('- ' + add )

make_sandwich('wpc', 'ice', 'stro')

# 8-14 cars
devide('8-14')
def car_profile(manufature, type, **flows):
    profile={}

    profile['manufature'] = manufature
    profile['type'] = type
    for key, value in flows.items():
        profile[key] = value

    return profile

car = car_profile('wuling', 'hongguang', lunzi=4, chenghao='qiumingshan')
print(car)

def per_profile(name, *interests):
    print(name)
    print(name + ' like:' )
    for interest in interests:
        print('- ' + interest)

per_profile('Xunkun Cai', 'chang', 'tiao', 'Rap', 'lanqiu', 'music')

# import
import profile as p
p.import_profile('Xunkun Cai', 'chang', 'tiao', 'Rap', 'lanqiu', 'music')


