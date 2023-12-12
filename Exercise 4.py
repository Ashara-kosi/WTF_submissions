#Write a program to produce the following output using for loop
# for i in range(0,5):
#     if i == 0 or i == 4:
#         print("+----+")
#     else:
#         print("\\    /")
#         print("/    \\")

#write a programe to produce the following output  using for loop
# for i in range(0,5):
#     print("**********")
    
#Write the code for the following for loop
#for i in range (1,7):


#  4 Write a program to produce the following output using for loops. Then 
# use a class constant to make it possible to change the number of lines in 
# the figure

# def generate_number_triangle(rows):
#     for i in range(1, 8):
        
#         print(str(i) * i)
# rows = 7
# generate_number_triangle(rows)

# Question 5 Write a method named pay that accepts two parameters: a real number 
# for a TA's salary, and an integer for the number of hours the TA worked 
# this week. The method should return how much money to pay the TA. 
# For example, the call pay(5.50, 6)
# should return 33.0. The TA should receive "overtime" pay of 1 ½ normal salary for any hours 
# above 8. For example, the call pay(4.00, 11) should return (4.00 * 8) + (6.00 * 3) or 50.0.

# def pay_Ta(salary, hourswork):
#     normalhours = 8
#     overtime = 1.5
#     if hourswork <=normalhours:
#         payment=salary * hourswork
#     else:
#         normalpayment = salary * normalhours
#         overtimepayment = salary * overtime * (hourswork - normalhours)
#         payment = normalpayment + overtimepayment
#     return payment
# salary = (4.00)
# hourswork = (11)
# result = pay_Ta(salary, hourswork)
# print(result)

# Question 6 Consider the following method for converting milliseconds into days:
# // converts milliseconds to days def toDays(millis): return millis / 1000.0 / 60.0 / 60.0 / 24.0
# Write a similar method named area that takes as a parameter the radius of a circle and that returns the area of the circle. For example, the call 
# area(2.0); should return 12.566370614359172. Recall that area can be computed as π times the radius squared and that 
# Python has a constant called math.pi

# import math 
# def area(radius):
#     return math.pi * radius**2
# radius = 2.0
# result = area(radius)
# print(result)

# Question 7 Copy and paste the following code into pythons IDLE script environment. low = 1
#  high = 1001 sum = 0 for i in range(low,high): sum += i print("sum = " , sum)
#  Modify the code to use a input to prompt the user for the values of low
# and high. Below is a sample execution in which the user asks for the same 
# values as in the original program (1 through 1000): low? 1 high? 1001 sum = 500500
# Below is an execution with different values for low and high: low? 300 high? 5298 sum = 13986903 You should exactly reproduce this format.

# low = 1
# high = 1001
# sum = 0
# for i in range(low,high):
#     sum += i
 
#     print("sum = " , sum)
        
# low = int(input("low?"))
# high = int(input("High?"))
# sum = 0
# for i in range(low,high):
#     sum += i
# print("sum = " , sum) 

# Question 8 Write a program using while loop that prompts the user for numbers until 
# the user types 0, then outputs their sum.

# #Initialize sum to zero
# total_sum = 0
#  #Use a while loop to repeatedly prompt the user for numbers
# while True:
#     #Prompt the user for input
#     user_input = input("Enter a number (enter 0 to finish): ")
 
#     #Convert the input to a float
#     number = float(user_input)
 
#     #Check if the entered number is 0
#     if number == 0:
#         break  #Exit the loop if the user enters 0
#     else:
#         #Add the entered number to the sum
#         total_sum += number
 
# # Output the sum
# print("Sum of the entered numbers:", total_sum)

# Question 9 Write a program using while loop that prompts the user for numbers until 
# the user types -1, then outputs their sum.

# #Initialize sum to zero
# total_sum = 0
#  #Use a while loop to repeatedly prompt the user for numbers
# while True:
#     #Prompt the user for input
#     user_input = input("Enter a number (enter 0 to finish): ")
 
#     #Convert the input to a float
#     number = float(user_input)
 
#     #Check if the entered number is 0
#     if number == -1:
#         break  #Exit the loop if the user enters 0
#     else:
#         #Add the entered number to the sum
#         total_sum += number
 
# # Output the sum
# print("Sum of the entered numbers:", total_sum)

# Question 10 .Write a method named repl that accepts a String and a number of 
# repetitions as parameters and returns the String concatenated that many 
# times. For example, the call repl("hello", 3) returns "hellohellohello". 
# If the number of repetitions is 0 or less, an empty string is returned.

# def repl(string, repetitions):
#     if repetitions <= 0:
#         return "" 
#     else:
#         return string * repetitions  
 
# result = repl("hello", 3)
# print(result)  # Output: "hellohellohello"


# Question 11 Write a method called printRange that accepts two integers as arguments and 
# prints the sequence of numbers between the two arguments, separated by 
# spaces. Print an increasing sequence if the first argument is smaller than 
# the second; otherwise, print a decreasing sequence. If the two numbers 
# are the same, that number should be printed by itself. Here are some 
# sample calls to printRange: 
# printRange(2, 7)
# printRange(19, 11)
# printRange(5, 5)
# The output produced should be the following: 
# 2 3 4 5 6 7 19 18 17 16 15 14 13 12 11 5

# def printRange(num1, num2):
#     if num1 < num2:
#         for num in range(num1, num2 + 1):
#             print(num, end=" ")
#     elif num1 > num2:
#         for num in range(num1, num2 - 1, -1):
#             print(num, end=" ")
#     else:
#         print(num1, end=" ")
 
# printRange(2, 7)
# printRange(19, 11)
# printRange(5, 5)

# Question 12 Write a method named smallestLargest that asks the user to enter numbers, 
# then prints the smallest and largest of all the numbers typed in by the 
# user. You may assume the user enters a valid number greater than 0 for 
# the number of numbers to read. Here is an example dialogue: 
# How many numbers do you want to enter? 4
# Number 1: 5
# Number 2: 11
# Number 3: -2
# Number 4: 3
# Smallest = -2

# def smallestLargest():
#     num_count = int(input("Enter the number of numbers to read: "))
#     smallest = float('inf')  
#     largest = float('-inf')  
 
#     for i in range(num_count):
#         user_input = float(input("Enter a number: "))
#         smallest = min(smallest, user_input)
#         largest = max(largest, user_input)
 
#     print("Smallest number:", smallest)
#     print("Largest number:", largest)
 
# smallestLargest()

#Question 13
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

# Question
# def numUnique(a,b,c):
#     unique_num = set([a, b, c])
#     print(len(unique_num))
# numUnique(3,4,5)
# print()
# numUnique(3,5,5)
# print()

