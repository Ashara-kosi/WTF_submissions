#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Write a function called showNumbers that takes a parameter called limit. It should printall the numbers between 0 and limit with a label to identify the even and odd numbers.For example, if the limit is 3, it should print:0 EVEN 1 ODD 2 EVEN 3 ODD
def showNumbers(limit):
    new_list=[]
    for num in range(0,limit+1):
        if num%2==0:
            new_list.append("EVEN")
        else:
            new_list.append("ODD")
    for value,i in enumerate(new_list,start=0):
        print(value,i)

(showNumbers(10))


# In[3]:


#2. Write a function that returns the sum of multiples of 3 and 5 between 0and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10,12, 15, 18, 20
def multiples(limit):
    new_list=[]
    for num in range(0,limit+1):
        if (num%3==0) or (num%5==0):
            new_list.append(num)
    return sum(new_list)

print(multiples(20))


# In[4]:


#3. Write a function called show_stars(rows). If rows is 5, it should print thefollowing:***************
def rows(row):
    rower="***"
    return row*rower

print(rows(5))   


# In[13]:


#4. Write a function that prints all the prime numbers between 0 and limit where limit is aparameter.
def prime_num(limit):
    new_list=[]
    for num in range(0, limit+1):
        if num > 1:
            for i in range(2, num):
                if num % i ==0:
                    break
                else:
                    
                    new_list.append(num)
                    break
    return new_list
print(prime_num(20))


# In[17]:


#5. Write a program (function!) that takes a list and returns a new list that contains all theelements of the first list minus all the duplicates
def no_dup(any_list):
    new_list = set(any_list)
    return list(new_list)

print(no_dup([1,2,3,3]))


# In[34]:


#6. Write a function to ask the user for a number and determine whether the number isprime or not.
def prime_asserter():
    num=int(input("Enter a number:"))
    message = ""
    for i in range(2,num):
        if num % i ==0:
            message= "{} is not a prime number"
            break
    if message == "":
        message= "{} is a prime number"
    return message.format(num)
print(prime_asserter())
num=[i for i in range(2,2)]
print(num)


# In[29]:


#7. Write a program that asks the user how many Fibonnaci numbers to generate and thengenerates them.


# In[38]:


#8. Write a function that ask the user for a string and print out whether this string is apalindrome or not.
def palindrome_asserter():
    a_str = input("Enter any word: ")
    if a_str==a_str[::-1]:
        message="{} is a palindrome"
    else:
        message="{} is not a palindrome"
    return message.format(a_str)
print(palindrome_asserter())


# In[ ]:


#9. Write a function that takes an ordered list of numbers (a list where the elements are inorder from smallest to largest) and another number.


# In[42]:


#10. Create a program that asks the user to enter their name and their age. Print out amessage addressed to them that tells them the year that they will turn 100 years old
def age_check():
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    year= int(input("what year are we in, Buddy: "))
    year_of_birth= year - user_age
    jubilee_year= year_of_birth + 100
    answer="Dear {}, you will turn 100 in the year {}."
    return answer.format(user_name,jubilee_year)
print(age_check())


# In[ ]:




