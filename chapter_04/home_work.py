#!/usr/bin/env python3
def devide(homework):
    print('')
    print('-------------------------------------------------------------------')
    print('|                           unit [' + homework + ']                             |')
    print('-------------------------------------------------------------------')
    print('')

# 4-1 pizza
devide('4-1')
pizza_list = ['pizza_one', 'pizza_two', 'pizza_three']
for pizza in pizza_list:
    print(pizza)
    print('I like ' + pizza + ' pizza')
print('I really love pizza')

# 列表解析
devide('列表解析')
squares = [value**2 for value in range(1,11)]
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])

# 列表复制
devide('列表复制')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)

# 4-10
devide('4-10')

number = list(range(2,11,2))
print(number)

print('The fisst three in the list are')
print(number[:3])
print('The items from the middle of the list are:')
print(number[1:4])
print('The last three items in the list are')
print(number[-3:])



# 4-11 your piza and my pizza

devide('4-11')
my_pizza_list = pizza_list[:]
print(my_pizza_list)
my_pizza_list.append('my love pizza')
print(my_pizza_list)
friend_pizza_list = pizza_list[:]
friend_pizza_list.append('friend love pizza')
print(friend_pizza_list)

print('My favorrite pizzas are:')
for pizza in my_pizza_list:
    print(pizza)

# 4-12
devide('4-12')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# 4-13 自助餐
devide('4-13')

yuan_zu = ('food_one', 'food_two', 'food_three')
for food in yuan_zu:
    print(food)

yuan_zu[0] = 'new_food_one'


yuan_zu = ('new_food_one', 'food_two', 'food_three')
for food in yuan_zu:
    print(food)



