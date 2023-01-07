#!/usr/bin/env python
# coding: utf-8

# In[1]:


#2 write a function that returns the sum of multiples of 3 and 5 between 0
#and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10,
#12, 15, 18, 20.
def sum_of_multiple(limit):
    for i in range(1,limit):
        if i % 3==0 or i % 5 ==0:
            print(i)
            
            
sum_of_multiple(24)


# In[2]:


#2 write a function that returns the sum of multiples of 3 and 5 between 0
#and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10,
#12, 15, 18, 20.
def sum_of_multiple(limit):
    for i in range(1,limit):
        if i % 3==0 or i % 5 ==0:
            print(i)
            
            
sum_of_multiple(24)


# In[17]:


#Write a function called show_stars(rows). If rows is 5, it should print thefollowing:***************
def show_star(row):
    if row == 5:
        print(10*'*')
    return


# In[16]:


#question 4 Write a function that prints all the prime numbers between 0 and limit where limit is aparameter.
def printprime_number(limit):
    for num in range(0,limit):
        if num >1:
            for i in range(2,num):
                if num % i ==0:
                    break
                else:
                    print(num)
printprime_number(12)


# In[ ]:


#5 Write a program (function!) that takes a list and returns a new list that contains all theelements
def without_duplicates():
    list = [10, 82, 3, 43, 50, 63, 71, 85, 910, 35, 43, 50, 61, 7, 78, 5]
    list = list2(dict.fromkeys(list))
    print(list)


# In[ ]:


#Write a function to ask the user for a number and determine whether the number isprime or not.
def prime_or_not(num):
    num = int(input("type in your digit!"))
    if (num % 2 == 0 and num % num >=1):
        print("it ia not a prime")
    else:
            print(num)
        
prime_or_not(3)    


# In[ ]:


#7Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
number = int(input("How many Fibonacci numbers would you like me to create?:"))
if (number <= 0):
    print("Number cannot be less than 1!")
else:
    FibonacciArray = [0]*number
    FibonacciArray[0] = 1
    FibonacciCounter = 2
    if (number > 1):
        FibonacciArray[1] = 1
    if (number > 2):
        while FibonacciCounter < number:
            FibonacciArray[FibonacciCounter] = FibonacciArray[FibonacciCounter - 2] + FibonacciArray[FibonacciCounter - 1]
            FibonacciCounter = FibonacciCounter + 1
    print(FibonacciArray)


# In[ ]:


#8 Write a function that ask the user for a string and print out whether this string is apalindrome or not. 

def palindrome():
    word = input("type i word").lower()
    if word[0:] == word[::-1]:
        print("this word is a palindrome")
    else:
            print("this word is not a palindrime")


# In[ ]:


#9. Write a function that takes an ordered list of numbers (a list where the elements are inorder from smallest to largest) and another number.
def ordered_list():
    list=[ 1,4,8,3,9,10, 23,4, 7, 9,21,87]
    list1 =list(set(list2))
    list2 = sort.list1
    print (list)
    return
ordered_list()

