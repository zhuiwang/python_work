#!/usr/bin/env python3
def devide(homework):
    print('')
    print('-------------------------------------------------------------------')
    print('|                           unit [' + homework + ']                             |')
    print('-------------------------------------------------------------------')
    print('')


# 2-3 个性化的消息
devide('2-3')
name = 'Eric'
print('Hello %s, would you like to learn sonme Python today?'% name)

# 2-4 调整名字的大小

devide('2-4')
'''name.upper(), name.lower(), name.title()'''
print(name.upper())
print(name.lower())
print(name.title())

# 2-5,6 名言
devide('2-5,6')
famous_personal = 'Albert Einstein'
famous_personal_said = '\"A person who nerver made a mistake nerver tried anything new.\"'
print(famous_personal + ' onie said,' + famous_personal_said)

# 2-7 剔除人名中空白
devide('2-7')
need_strip_name = '\t\tname\t\t\n'
print('start' + need_strip_name.rstrip() + 'end')
print('start' + need_strip_name.lstrip() + 'end')
print('start' + need_strip_name.strip() + 'end')

# 2-8 数字8
devide('2-8')
print(1+7)
print(2**3)
print(2*4)
print(16//2)

# 2-9 最喜欢的数字
devide('2-9')
most_love_number = 5
print('my most love number is %d' % most_love_number)

# 2-10 添加注释

# 2-11 import this
devide('2-11')
import this
