# print("+----+")
# for i in range(3):
#     print("\\    /")
#     print("/    \\")
# print("+----+")

# for i in range(1,6):
#     print('*' * 10)

# for a in range(1,7):
#     print (a)
# for b in range(2,14,2):
#     print(b)
# for c in range(4,94,15):
#     print(c)
# for d in range(30,-30,-10):
#     print(d)
# for e in range(-7,17,4):
#     print(e)
# for f in range(97,79,-3):
#     print(f)
# for g in range(-4,104,18):
#     print(g)

# for x in range(1,8):
#     print(str(x) * x)

# def pay(x,y):
#     overtime = True
#     if y > 8:
#         ans = (1.5 * x) * (y - 8) + (x * 8)
#         print(ans)
#     else:
#         print(x * y)
# pay(4, 11)

# import math
# def area(radius):
#     print(math.pi * (radius**2))
# area(2.0)
# print()

# low = int(input("Low: "))
# high = int(input("High: "))
# sum = 0
# for i in range(low,high):
#     sum += i
# print("sum = " , sum)

# total_num = 0
# while True:
#     userInput = float(input("Enter a number: "))
#     if userInput == 0:
#         break
#     total_num += userInput
# print("Sum of entries: ", total_num)

# total_num = 0
# while True:
#     userInput = float(input("Enter a number (negative digit): "))
#     if userInput == -1:
#         break
#     total_num += userInput
# print("Sum of entries: ", total_num)

# string = "Hello"
# y = string.replace("Hello", "Hello"*3)
# print(y)

# def repl(string,times):
#     if times <=0:
#         print("")
#     else:
#         print(string * times)
# repl("Hello",3)
# print()

# def printRange(a,b):
#     if a < b:
#         for i in range(a, b + 1):
#             print(i, end=" ")
#     elif a > b:
#         for i in range(a, b - 1, -1):
#             print(i, end=" ")
#     else:
#         print(a)
# printRange(3,10)
# print()
# printRange(10,4)
# print()
# printRange(9,9)

# def smallestLargest():
#     total_num = int(input("How many numbers would you like to enter? "))
#     smallest = float('inf')
#     largest = float('-inf')
#     for i in range(1, total_num + 1):
#         num = float(input(f"Number {i}: "))
#         smallest = min(smallest,num)
#         largest = max(largest, num)
#     print(f"Smallest = {smallest}")
#     print(f"Largest = {largest}")
# smallestLargest()

# def printAverage():
#     total = 0
#     count = 0
#     while True:
#         num = float(input("Input a number: "))
#         if num < 0:
#             break
#         total += num
#         count += 1
#     if count > 0:
#         average = total / count
#         print(f"Average was {average}")
#     else:
#         print("No nonnegative numbers given.")
# printAverage()

# def numUnique(a,b,c):
#     unique_num = set([a, b, c])
#     print(len(unique_num))
# numUnique(3,4,5)
# print()
# numUnique(3,5,5)
# print()

# import random
# def dice_roll():
#     return random.randint(1,6)
# def roll_till_7():
#     tries = 0
#     while True:
#         dice1 = dice_roll()
#         dice2 = dice_roll()
#         total_roll = dice1 + dice2
#         print(f"{dice1} + {dice2} = {total_roll}")
#         tries += 1
#         if total_roll == 7:
#             break
#     print(f"You won after {tries} tries!")
# roll_till_7()