# write a program to produce the following output using for loop
# Q1
# def symbols():
#   sym=['+----+', '\\   /','/   \\','\\   /','/   \\','\\   /','/   \\','+----+']
#   for i in sym:
#     print(i)
# symbols()


# Q2
# def special_symbol():
#          symb_s=['**********','**********','**********','**********','**********']
#          for i in symb_s:
#              print(i)
# special_symbol()

# Q3
# for a in range(1,7):
#      print(a)
# for b in range(2,13,2):
#   print(b)
# for c in range(4,80,15):
#   print(c)
# for d in range(30,-21,-10):
#    print(d)
# for e in range(-1,13,4):
#    print(e)
# for f in range (-2,86,18):
#    print(f)
# for g in range(-2,86,18):
#     print (g)


# Q4
# for row in range(1,8):
#   for col in range(0,row):
#         print(row,end=" ")    
#   print()  

# Q5
# def pay(rate, hrs):
#     salary= float(rate*hrs)
#     print(salary)
# pay(5.50,6)

# for above normal hours
# def pay(rate, hrs):
#      if hrs> 8:
#          salary= float(1.5*(hrs-8) + (rate*8))
#          print(salary)
#      if hrs<8 >0:
#          salary= float(rate*hrs)
#          print(salary)
#      else:
#          print('error')
    
# pay(11.50,6)

# Q6

# import math

# def cir_area(radius):
#       cir_area= [radius*radius* math.pi]
#       print (cir_area)
# cir_area(2.0)


# Q7 modify the following code using input function
# low = 1
# high = 1001
# sum = 0
# for i in range(low,high):
#  sum += i
# print("sum = " , sum)
#  
# solution

# low= int(input('low?'))
# high= int(input('high?'))
# sum=0
# for i in range (low,high):
#      sum += i
# print("sum = " , sum)

#  Write a program using while loop that prompts the user for numbers until 
# the user types 0, then outputs their sum.

# Q8 Write a program using while loop

# def abc():
#      list1=[]
#      x=int(input('enter numbers\n'))
#      list1.append(x)
#      while x!=0:
#          x=int(input('enter numbers\n'))
#          list1.append(x)
#          if x==0:
#              print(list1)
#              add=sum(list1)
#              print('Sum =',add)
#              break
# abc()

# Q9 While loop

# def abc():
#      list2=[]
#      x=int(input('enter numbers\n'))
#      list2.append(x)
#      while x!=-1:
#          x=int(input('enter numbers\n'))
#          list2.append(x)
#          if x==-1:
#              print(list2)
#              add=sum(list2)
#              print('Sum =',add + 1)
#              break
# abc()

# Q10 create repl method that accepts string and a number of repetitions

# def repl(str, repetitions):
#      if repetitions > 0:
#          print(str* repetitions) 
#      else:
#          print()
# repl('hello', 3)
# repl('hello',0)
# repl('hello',6)

# Q11 PRINT RANGE METHOD

def printRange(start,end):
     if start< end:
        for i in range(start, end +1):
           print(i, end=" ")
     elif start > end:
        for i in range(start, end -1, -1):
           print(i,end=" ")
     else:
       start == end
       print(start)
    
printRange(19,11)
# printRange(2,7)
# printRange(5,5)

# Q12 smallestLargest number


# def smallestLargest():
#     Inp_numbers = int(input("How many numbers do you want to enter? "))
#     i= (i+1)
#     numbers = int(input(f"Number {i + 1} ")) 
#     for i in range(Inp_numbers):
#        smallest = min(numbers)
#        largest = max(numbers)
#     print(f"Smallest = {smallest}")
#     print(f"Largest = {largest}")

# smallestLargest()

# Q13

# def printAverage():
#   numbers = []
#   while True:
#     number = float(input("Type a number: "))
#     if number < 0:
#       break
#     numbers.append(number)
#   else: 
#       print("No non-negative numbers were entered.")
#       return
#   average = sum(numbers) / len(numbers)
#   print(f"Average was {average:.1f}")

# Q14
# def numUnique(a, b, c):
#   unique_values = set()
#   unique_values.add(a)
#   unique_values.add(b)
#   unique_values.add(c)
#   return len(unique_values)
# numUnique(2, 3, 5)

# Q15

# import random

# dice1, dice2, total, tries = 0, 0, 0, 0
# while total != 7:
#   dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
#   total = dice1 + dice2
#   tries += 1
#   print(f"{dice1} + {dice2} = {total}")
# print(f"You won after {tries} tries")

# Q13
total = 0
    count = 0
    while True:
        num = float(input("Input a number: "))
        if num < 0:
            break
        total += num
        count += 1
    if count > 0:
        average = total / count
        print(f"Average was {average}")
    else:
        print("No nonnegative numbers given.")
printAverage()

# Q14
def numUnique(a,b,c):
    unique_num = set([a, b, c])
    print(len(unique_num))
numUnique(3,4,5)
print()
numUnique(3,5,5)
print()