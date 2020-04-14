#!/usr/bin/env python3.7

import random


print("Please input a number for Adding")
end_number=input("Please input a number exp: 10 15 20 25 30 25 40 ... 100 : ")
end_check_number=int(end_number)
print("Your input number is: %d" % end_check_number)
print("Start your Math caculate ... ...")
point=0
test_num=0
for j in range(3,end_check_number+1):
    for i in range(1,j+1):
        test_num=test_num+1
        print("\n    Test: %d" % test_num)
        for_add_number=random.randint(0,j)
        print("    Which number ? + %d = %d "% (for_add_number,j))
        print("    Which number %d = %d + ? "% (j,for_add_number))
        answer=input("\n    Please input your number: ")
        if answer.isdigit():
            answer_number=int(answer)
            answer_add=for_add_number+answer_number

            if (answer_add == j):
                print("        You are right!")
                point = point + 1
                print("        Your Point now: %d\n" % point)
            else:
                print("        False answer")
                print("        Your Point now: %d\n" % point)
        else:
            print("        Your answer is not a digit !!!")
            print("        False answer")
            print("        Your Point now: %d\n" % point)

print("\n Your final score is %d" % point)

