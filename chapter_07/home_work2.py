#!/usr/bin/env python3
def devide(homework):
    print('')
    print('-------------------------------------------------------------------')
    print('|                           unit [' + homework + ']                             |')
    print('-------------------------------------------------------------------')
    print('')


# 7-8

sandwich_orders = [ 'san', 'van', 'chi', 'pastrami', 'da', 'pastrami', 'pastrami']
finished_sandwich = []

for sandwich in sandwich_orders:
    print("I mading " + sandwich + " for you ing...." )
    finished_sandwich.append(sandwich)

print(finished_sandwich)

# 7-9 pastrami
print('pastrami has been sold out !')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

# 7-10 wanner to go
places = []
while True:
    place = input('you could visit one place in the world, where would you go?')
    if place == 'quit':
        break

    places.append(place)

print(places)


