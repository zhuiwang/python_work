#!/usr/bin/env python3
def devide(homework):
    print('')
    print('-------------------------------------------------------------------')
    print('|                           unit [' + homework + ']                             |')
    print('-------------------------------------------------------------------')
    print('')


# 7-1
devide('7-1')

car_name = input("what kind of cat s would you want to get ?")
print("I want to get " + car_name)

# 7-2
devide('7-2')
num_of_person = input("How manny person")
if int(num_of_person) > 8:
    print("Ther is no table")
else:
    print("please get in")

# 7-3
devide('7-3')
num = input("please in put a number ")
if int(num)%10 == 0:
    print("")

# 7-4 pizza
devide('7-4')
while True:
    peiliao = input("Please in put a pizza pei liao:")

    if peiliao == 'quit':
        break
    else:
        print("We will add " + peiliao + " to pizza")

# 7-8 电影票
devide('7-8')
while True:
    age = input("How old are you ?")
    if int(age) <= 3:
        print("Your tickets is free")
    elif int(age) <= 12:
        print("Yor tickets is $10")
    else:
        print("Yor tickst is $15")
