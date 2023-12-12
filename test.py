#print("hello world")
#print("My name is John")
#a = float(input("how much do I sell?"))
#print(a)
#ab = 2.34
#c = int(ab)
#print(c)

#lists
#list_a = [2,4,3,6,78,89,76,45,67]
#list_b = ['girl','boy',57,87,56.76,89.0,45]
#list_c = ['boy','girl','dog','sheep']
#list_c.sort()
#print(list_c)
#print(len(list_b))
#print(list_a[0:5])
#print(list_a[-2])
#d = 35 // 7
#e = 145 % 10
#print(d)
#print(e)
#print('My name is Keef \t I am a girl')
#print("Keef", "Girl", sep=", ", end=".")
#print("Kafayat said 'I am a girl'")
#name = input("What is your name")
#print(name)
#print(f'{name} went to the market')
#print('{1} {2} {0}'.format('Directions','Read','The'))
#a = int(input("please enter a number"))
#print(a)
#b = int(input("please enter a second number"))
#print(b)
#c=a+b
#print(c)
#Num1=int(input("please enter a number"))
#Num2=int(input("please enter a second number"))
#Ans= Num1 + Num2
#print(f'{Num1}+{Num2}={Ans}') 
#print(f'{Ans}')

# dict1 = {1:'Kosi',2:'Kate',3:'John',4:['James','Paul','Mary']}
# print(dict1[1])
# print(dict1[4])
#dict_empty = {}
#dict_empty['James']=5
#dict_empty['Andrew']=6
#print(dict_empty)
#print(dict_empty.get('James'))

# a=55
# b=100
# if a > b:
#     print('The first value is greater')
# else:
#     print('The second value is greater')

# a = 33
# b = 33
# if b > a:
#     print('b is greater than a')
# elif a == b:
#     print('the values are equal')
# else:
#     print('a is greater')

# number = int(input('please put in a number'))

# if number % 2 == 0:
#     print('even number')
# else:
#     print('odd number')

#Code for loops (For loop)
# character = 'ABCDEFGHIJKLMNOP'

# for i in character:
#     print(i)

# list1 = [2,4,5,6,7,8,9,0,1,2,4]
# newlist = []
# for item in iter(list1):
#     newvalue = item * item
#     newlist.append(newvalue)
# print(newlist)

# for i in range(2,30):
#     print(i)

# for i in range(2,30,3):
#     print(i)
# for i in range(50,30,-2):
#     print(i)

# converting tuple to list and list to tuple 
# tuple1 = (1,2,3,4,5,5)
# list24 = list(tuple1)
# print(list24)
# list_h = [3,4,6,7,8,9,1]
# print(tuple(list_h))

#print(tuple('python'))

#unpacking a tuple
# fruits = ("apple", "banana", "cherry")
# (green,yellow,red) = fruits
# print(green)

#use asterisk * to assign a value to the rest
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green,yellow,*red) = fruits
# print(red)

#set returns only unique values. You can use it to extract unique values from a list
# set1 = {2,3,3,4,5,5,6,7,8,8,8}
# print(set1)
# list_g = [4,5,6,6,6,7,7]
# print(set(list_g))
# set1.add(9)
# print(set1)

# #If you don't your set to be immutable, use frozenset
# set2 = frozenset({2,3,4,4,5,6,6,7})

# code for while loop
# box = 0
# while (box <10):
#     box = box + 1
#     print(box)

""" Write guess dice number program that
Randomly initialize dice variable with a value between [1,6]
Keep asking the user to guess the number until he gets it right """

#first way to do it
# guess = int(input('Please put in a number between 1-6'))
#correct_num = 5
# game = False
# while (guess <= 6 and game == False):
#     if guess == correct_num:
#         print('Yay, you have won the game')
#         game = True
#     else:
#         print('Sorry, try again')
#         guess = int(input('Please put in a number between 1-6'))

#second way to do it
# import random
# guess = int(input('Please put in a number between 1-6'))
# correct_num = random.randint(1,6)
#game = False
# while (guess <= 6 and game == False):
#     if guess == correct_num:
#         print('Yay, you have won the game')
#         game = True
#     else:
#         print('Sorry, try again')
#         guess = int(input('Please put in a number between 1-6'))

"""write a program that prints the first 10 numbers in the fibonacci series,
A Fibonacci series is a series of numbers in which each number 
(fibonacci number) is the sum of the two preceding numbers.
[0 1 1 2 3 5 8 13 21 34]"""

#fibon = [0,1]
# while (len(fibon)< 10):
#     sum = fibon[-1] + fibon[-2]
#     fibon.append(sum)
# print(fibon)

#to know the type/class of a variable
#print(type(fibon))

""" Functions """
# def laughter():
#     print('HAHA'*5)
# laughter()

# fibon = [0,1]
# def fibonacci_Series(fibon):
#     while (len(fibon)< 10):
#        sum = fibon[-1] + fibon[-2]
#        fibon.append(sum)
#     return fibon
# list1 = [5,6]
# print(fibonacci_Series(list1))

""" write a program that:
1. Gets two input numbers X and Y from the user.
2. Find the numbers which are divisible by 7 and multiple of 5,
between X and Y (both)"""

# X=int(input('enter number 1'))
# Y=int(input('enter number 1'))
# b= []
# for i in range(X,Y):
#     if i%35 == 0:
#         b.append(i)
# print(b)

""" to store the above in a function"""
# X=int(input('enter number 1\n'))
# Y=int(input('enter number 2\n'))
# def ma_th(a,b):     
#     bes=[]     
#     for i in range(a,b):
#         if i%35==0:
#             bes.append(i)
#     return(bes)
# print(ma_th(X,Y))

"""testing pronic"""
# list11=[1,2,3,4,5,6,7,8,9,10]
# list33=[]
# for i in range(0,len(list11)-1):
#     prod=list11[i]*list11[i+1]
#     list33.append(prod)
# print(list33)

""" Write this function:
is_pronic(num): takes a number and returns whether this number is pronic or not.
A number is pronic if it is a product of two consecutive numbers"""

# X=int(input('enter a number\n'))
# def is_pronic(num):
#     list11=[]
#     list33=[]
#     list44=[]
#     for i in range(0,num):
#         list11.append(i)
#     list33=list11
#     for i in range(0,len(list33)-1):
#        prod=list33[i]*list33[i+1]
#        list44.append(prod)
#     Y=list44
#     if num in Y:
#         print('pronic')
#     else:
#         print('not pronic')
# is_pronic(X)

"""code for getting a prime number"""
# num=int(input('enter a number:\n'))
# prime_factors=[]
# for i in range (1,num+1):
#       if num%i==0:
#          prime_factors.append(i)
# if len(prime_factors)==2:
#     print(f'{num} is a prime number')
# else: 
#     print(f'{num} is not a prime number')

"""nested loops"""
# for row in range(0,10):
#       for col in range(0,row+1):
#         print('*',end=" ")
# print()

# for num in range(1,10):
#     print(f'Multiplication table for {num}')
#     for j in range(1,10):
#         ans=num * j
#         print(f'{num} * {j} = {ans}')

"""without list comprehension"""
# fruits = ['banana','apple','orange','mangoes','lime']
# x = []
# for fruit in fruits:
#     if 'a' in fruit:
#         x.append(fruit)
# print(x)

"""with list comprehension"""
# fruits = ['banana','apple','orange','mangoes','lime']
# a_fruits = [x for x in fruits if 'a' in x]
# print(a_fruits)

# list1 = [2,4,5,6,7,8,9,0,1,2,4]
# newlist = [j*2 for j in list1]
# print(newlist)

"""enumerate"""
# list1 = [2,4,5,6,7,8,9,0,1,2,4]
# newlist = [j for j in enumerate(list1)]
# print(newlist)

"""exception when you know the likely error"""
# def divide(x,y):
#     try:
#         ans = x//y
#         print(f'your answer is {ans}')
#     except ZeroDivisionError:
#         print(f'Hello, you are trying to divide by zero')
# print(divide(5,0))

"""exception when you don't know the error"""
# def divide(x,y):
#     try:
#         ans = x//y
#         print(f'your answer is {ans}')
#     except Exception as e:
#         print(f'The error is {e}')
# print(divide(5,0))







