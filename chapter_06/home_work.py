#!/usr/bin/env python3
def devide(homework):
    print('')
    print('-------------------------------------------------------------------')
    print('|                           unit [' + homework + ']                             |')
    print('-------------------------------------------------------------------')
    print('')

# 6-1
devide('6-1')

person = {
    'first_name': 'chen',
    'last_name': 'zhao',
    'age': '23',
    'city': 'beijing'
}
print(person)

for key,value in person.items():
    print('Key is ' + key)
    print('Value is ' + value)

print(person.keys())
print(sorted(person.keys()))

for key in person.keys():
    print(key)


for key in sorted((person.keys())):
    print(key)

for value in person.values():
    print(value)

# 6-5
devide('6-5')
reiver_dict = {
    'changjiang': 'china',
    'niluohe': 'feizhou',
    'meigonghe': 'miandian'
}

for reiver,city in reiver_dict.items():
    print(reiver + ' is in ' + city)

# 6-6
devide('6-6')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

name_list = ['jen', 'sarah', 'hes']

for name in name_list:
    if name in favorite_languages.keys():
        print('Thanks for ' + name + ' accept!')
    else:
        print('invite ' + name + ' to have diaocha')

# 6-7
devide('6-7')
person1 = {
    'first_name': 'chen',
    'last_name': 'zhao',
    'age': '23',
    'city': 'beijing'
}
person2 = {
    'first_name': 'man',
    'last_name': 'zhang',
    'age': '23',
    'city': 'wuhan'
}

person_list = [person1, person2]

print(person_list)
for person in person_list:
    for key,value in person.items():
        print(key + ': ' + value)

# 6-8
devide('6-8')
dog = {'name': 'lengwa',
       'zhuren': 'person1',
       'leixing': 'pet'}

cat = {'name': 'erdan',
       'zhuren': 'person2',
       'leixing': 'pet'}

mouse = {'name': 'taoqi',
         'zhuren': 'person3',
         'leixing': 'none'}

pets = [dog, cat, mouse]
for pet in pets:
    for key,value in pet.items():
        print(key + ': ' + value)

# 6-9
devide('6-9')

favorite_place = {'zhangyu': ['xian', 'beijing'],
                  'zhaofan': ['chongqing'],
                  'wangmin': ['shanghai', 'beijing', 'sichuan']}

for key,value in favorite_place.items():
    print(key + "'s favorite place is:")
    for place in value:
        print(place)


# 6-11 city
devide('6-11')

beijing = {'country': 'china',
           'population': '1000',
           'zhou': 'yazhou'}

seaito = {'country': 'usa',
           'population': '100',
           'zhou': 'meizhou'}

touku = {'country': 'japan',
           'population': '500',
           'zhou': 'yazhou'}

cities = {'beijing': beijing,
          'seaito': seaito,
          'touko': touku}

print(cities)

for key,value in cities.items():
    print(key + ': ')
    print(value)
    for key_2,otto in value.items():
        print(key_2 + ': ' + otto)
