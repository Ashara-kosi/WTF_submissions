#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.	Write a function to calculate the multiplication and sum of two numbers.
def calc(num_1,num_2):
    multi_ans=num_1 * num_2
    sum=num_1 + num_2
    return("The sum of the two numbers is {} and the product of the two numbers is {}".format(sum,multi_ans))


           
print(calc(num_1 = 2,num_2 = 3))


# In[25]:


#2.	Write a function to print the sum of the current number and the previous numberr
def add_func(any_list,element):
    sum= element
    i = 0
    while i<len(any_list):
        if any_list[i]==element:
            break
        i+=1
        
    sum+=any_list[i-1]
    return sum

print(add_func([1,2,3,4,5,6],6))


# In[6]:


#3.	Write a function to print characters from a string that are present at an even index number
def even_str(any_str):
    start=0
    end=len(any_str)
    new_str=""
    #print(end)
    while start<end:
        if start%2==0:
            new_str+=any_str[start]
        start+=1
    return(new_str)
    
print(even_str('madam'))
    


# In[13]:


#4.	Write a function to rremove first characters from a string
def first_rem(any_str):
    new_str =""
    count = 1
    while count < len(any_str):
        new_str += any_str[count]
        count+=1
    return new_str
print(first_rem("madam"))


# In[14]:


def first_rem(any_str):
    new_str= any_str[1:]
    return new_str
print(first_rem("madam"))


# In[18]:


#5.	Write a function to check if the first and last number of a list is the same
def checker(a_list):
    ans=a_list[0]== a_list[-1]
    return ans
print(checker([0,1,2,4]))
print(checker([0,1,2,0]))


# In[19]:


#Write a function to print multiplication table from 1 to 10
def tables(stop_range):
    for num in range(1,stop_range):
        print("Multiplication Table for {}".format(num))
        for i in range(1,13):
            print("{} * {} = ".format(num,i) ,num * i)
        print("\n")
tables(11)


# In[23]:


#7.	Given a two list of numbers, write a function to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
def compiler(ist_list,second_list):
    new_list=[]
    for num in ist_list:
        if num%2==0:
            new_list.append(num)
    for num in second_list:
        if num%2!=0:
            new_list.append(num)
    return new_list
print(compiler([1,2,3,4,5,6],[7,8,9,10,11,23]))


# In[ ]:




