#!/usr/bin/env python
# coding: utf-8




#1.	Write a function to calculate the multiplication and sum of two numbers.
def sum_mul(num_1,num_2):
    multi_ans=num_1 * num_2
    sum_ans=num_1 + num_2
    return f"The sum of the two numbers is {sum_ans} and the product of the two numbers is {multi_ans}"


           
print(sum_mul(4,5))





#2.	Write a function to print the sum of the current number and the previous numberr
def addition(any_list,item):
    sum= item
    i = 0
    while i<len(any_list):
        if any_list[i]==item:
            break
        i+=1
        
    sum+=any_list[i-1]
    return sum

print(addition([1,2,3,4,5,6],6))





#3.	Write a function to print characters from a string that are present at an even index number
def even_string(string):
    start=0
    end=len(string)
    new_str=""

    while start<end:
        if start%2==0:
            new_str+=string[start]
        start+=1
    return(new_str)
    
print(even_string('madam'))
    





#4.	Write a function to rremove first characters from a string
def remover(string):
    new_str =""
    count = 1
    while count < len(string):
        new_str += remover[count]
        count+=1
    return new_str
print(remover("madam"))





def remover(string):
    new_str= string[1:]
    return new_str
print(remover("madam"))





#5.	Write a function to check if the first and last number of a list is the same
def checker(list_1):
    ans=list_1[0]== list_1[-1]
    return ans
print(checker([0,1,6,7,9,4]))
print(checker([0,1,2,0]))





#Write a function to print multiplication table from 1 to 10
def tables(stop_range):
    for num in range(1,stop_range):
        print f"Multiplication Table for {num}"
        for i in range(1,13):
            print("{} * {} = ".format(num,i) ,num * i)
        print("\n")
tables(11)




#7.	Given a two list of numbers, write a function to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
def compiler(a_list,b_list):
    new_list=[]
    for num in a_list:
        if num%2==0:
            new_list.append(num)
    for num in b_list:
        if num%2!=0:
            new_list.append(num)
    return new_list
print(compiler([1,2,3,4,5,6],[7,8,9,10,11,23]))


# In[ ]:




