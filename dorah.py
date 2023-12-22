#a= 1+3*4
#b= (1+3)*4
#print(a)
#print(b)
#print(a*b)
#print(a/b)
#print("My name is Dorah",sep = ",", end ="o")
#print("I find eating cake awesome!\nIt's tasty!")
#print("Cool stuff\tHuh!")
#print('She said, "Awesome"')
#name= input("What is your name?")
#print('{1} {2} {0}'.format('Directions','Read','The'))
#dprint(f'{name} went to the market')
#a=int(input('Please put in the number'))
#b= int(input('Please put in the number'))
#Ans = a+b
# #print(f'{a}+{b}={Ans}')
# a=input('What is your first name?')
# b= input('What is your second name?')
# print(f'{a} {b} is my name')
#a=float(input("How many mangoes are in the basket?"))
#print(a)

#lists
#list_a =[2,4,3,5,6,78,89,76,45,67]
#list_b =['girl','boy',57,87,56.76,89.0,45]
#list_c = ['a','b','d','c']
#print(list_a[5])
#print (list_b[6])
#print(list_c[1], list_c[3],list_b[0])
#list_a.pop(1)
#list_a.sort(reverse=True)
#list3=list_a.copy()
#list_a.append('huge')
#print(list_a[1:4])
#print(list_a[:-1])
# for i in range(30,2,-2):
#     print(i)
# box = 0
# while(box<10):
#     box = box+1
#     print(box)
#Write guess dice number program that randomly initialize dice variable  with a value between [1,6],
# keeps asking the user to guess the number until he/she gets it right
# guess = int(input('Please put in a number between 1-6:'))
# correct_num = 5
# game = False
# while(guess <= 6 and game == False):
#     if guess == correct_num:
#         print('Yay, you have won the game')
#         game = True
#     else:
#         print('Sorry, try again')
#         guess = int(input('Please put in a number between 1-6:'))
# import random

# guess = int(input('Please put in a number between 1-6:'))
# correct_num = random.randint(1,6)
# game = False
# while (guess <= 6 and game == False):
#     if guess == correct_num:
#         print('Yay, you have won the game')
#         game = True
#     else:
#         print('Sorry, try again')
#         guess = int(input('Please put in a number between 1-6:'))
fibon = [0,1]
while(len(fibon)<10):
    sum =fibon[-1] + fibon[-2]
    fibon.append(sum)
print(fibon)
# def fun():
#     print('Welcome to GFG')

# fun()
# def laughter():
#     print('HAHAHA'*5)

# laughter()
# fibon =[0,1]
# def fibonacciSeries(fibon):
#     while (len(fibon)<10):
#         sum = fibon[-1] + fibon[-2]
#         fibon.append(sum)
#     return fibon

# list1 = [5,6]
# print(fibonacciSeries(list1))
# for row in range(0,10):
#     for col in range(0,row+1):
#         print('*', end= " ")
#     print()
# for num in range(1,13):
#     print(f'Multiplication table for {num}')
#     for j in range(1,13):
#         ans = num * j
#         print(f'{num}*{j} = {ans}')
