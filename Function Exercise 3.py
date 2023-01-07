# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:12:08 2022

@author: Olajumoke Falowo
"""
#Question 1
#function to multiply and sum two numbers
def multiply_sum(x,y):
    return(x*y, x+y)
multiply_sum(3,4)

#Question 2
#function to add current and previous number
def sum_num(currentnum):
    previousnum = currentnum - 1
    print('the sum is')
    return(currentnum + previousnum)

#Question 3
#function to output characters of a string at even index position
def even_index_str(string):
    i = 0
    even_num = []
    while i < len(string):
        even_num.append(string[i])
        i = i + 2
        print(even_num)
              
even_index_str('olajumoke')

#Question 4
#function to remove first characters from a string
def my_string(string)
    return(string[1:])
my_string('techsters')

#Question 5
#function to check if first and last number of a list are the same
def check_list(list):
    if list[0] == list[-1]:
        return('they are the same')
    else:
        return('they are not the same') 
list = [11,2,33,4,11]
check_list(list )

#Question 6
#function to print multiplication table 1 to 10
def multiplication_table(a, b):
    for i in range(a, b+1):
        for num in range(1, 13):
            multiply = i * num
            print(i,'*', num, '=', multiply)
multiply(1,10)

#Question 7
#function adding even and odd numbers to another list
def odd_even_num(odd_list, even_list):
    new_list = []
    for i in odd_list:
        if i % 2 == 1:
            new_list.append(i)
    for i in even_list:
         if i % 2 == 0:
            new_list.append(i)
    return(new_list)
odd_list = [1,2,3,4,5]
even_list = [4,6,2,7]
odd_even_num(odd_list, even_list)
                
            
            