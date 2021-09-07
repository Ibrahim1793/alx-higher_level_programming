#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
number1 = number[-1]
if int(number1) > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, number1 ))
elif int(number1) == 5:
    print("Last digit of {} is {} and is 0".format(number, number1 ))
elif (int(number1) < 6) and (int(number1) !=0):
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, number1 ))
