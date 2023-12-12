# # # # #start by defining variable and print the variable for result
# # # # # s=35%5
# # # # # y=150%4
# # # # # print (s)
# # # # # print(y)

# # # # #Use double quote at begining of string when we have a single quotated statement in btw text or string
# # # #print('''Blessing said, 'she is a data scientis''')

# # # #Input is use when we require info from users
# # # #name=input('what is your name')
# # # #print(name)
# # # d=int(input('what is the first no'))
# # # f=int(input('what is the second no'))
# # # answer=(d+f)
# # # print(f'{d}+{f}={answer}')



# # # #String.Format is use to arrange string in the format we want using no. py recognize no starting from 0.
# # # #print('{1} {2} {0}'.format('directions','Read','The'))
# # # print(f'{name} went to the market')

# # # #in defining a variable, use string against string and vs versa(but u can combine string and numeric using ,) and underscore for the name of variable. 
# # #x='icecream is my favourite' +'.'
# # #print (x)
# # ice_cream=('vanilla', 'chocolate', 'strawbery')
# # #print (ice_cream)
# # t,r,i = ice_cream
# # print (i)
#data_science=['coding','visuals','insight']
# data_science.append('blessing')
# print (data_science)
#data_science[1]

#Data structure can be list,tuple,dictionary and set
#List is seperted by , and in this [], each data set in the list is an element
#indexing is getting the position of an element
list_a=[1,4,5,7,2,5,34,78,9,9.0]
List_b=['man',7.8,9,5,7,3,0.1,'eggs']
list_c=['a','b','c','d','o','r','e','y','i']
list_f=['blessing',[1,4,7],[45.0],['mind','clean','fish'],[6,8,5,4]]
print(list_f[3][2][3])
#print(list_c[1],list_c[4],list_c[7])
# print(list_a[:5])
# print(List_b[-5])
# #slicing is getting a subset from an element
# print(List_b[0][2])


#Append and pop is use to add element to list (last part of list) and remove element from list (base on element position)
# list_a.append('boy')
# list_a.pop(10)
# list_a.sort()
# list_a.sort(reverse=False)
# print(list_a)

#tuples are immutable ie cannot be change and it uses , and ()
var_bless=(1,3,4,5)
var_bless[2]=9
print(var_bless)



