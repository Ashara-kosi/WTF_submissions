#x=input("enter your firstname :")
#print (x)
#print("your name is " +" " +x)
#import math
#print(100%3)
#print(float(100//3))

#print('{1},{0}'.format('hello''habi'))
#print('{1},{2},{0}').format('directions','the',)
#print(x)
'''x=input("enter first name:")
y=input("enter second name:")
#sum=x+y
#print('{1},{0}'.format('y','x'))
print(x,y)
#print(sum)'''

'''list_1=[21,46,7,90,76]
list_2=['cat','dog','sheep','queen']
list_1.append('prince')
list_1.pop(2)
list_2.sort(reverse=False)
list3=list_2.copy()
list3.append('hello')
list_4=['girl',[2,3,4],5,6,7,[8,9,0],32]

#print(list_1[4],list_2[2]+'s')
print(list3[-2])
print(list_1[1:4])
print(list_2[2:])
print(list_2[:3])
print(list_4[0][3])
print(list_4[5][2])
print(len(list_4))

dict1={'jem:"lem",2:henm'}'''
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
print(x)

'''a=int(input("enter a"))
b=int(input("enter b"))
if b>a:
    print(b +"is greater than"+ a)
elif a==b:
    print(a+"and"+b+"are equal")
else:
    print(a+"is greater than "+b)'''

'''a=int(input("enter a"))
if a % 2==0:
    print("your input is even")
else:
    print("Your number is odd")'''

'''list1=[1,2,4,5,6,7,9,8,7,3,4,5]
newlist=[]
for item in iter(list1):
    newvalue= item * 2
    newlist.append(newvalue)
print(newlist)'''

'''character='wdgfuegyfv'
for characters in character:
    print(characters)''' 

'''for i in range(30,2,-1):
    print(i)'''
'''box=0
while(box<10):
    box=box+1
    print(box)'''
'''import random
guess=int(input("please input a value between 1 and 6:"))
correct_num=random.randint(1,6)
game=False
while(guess<=6 and game==False):
    if guess== correct_num:
        print("you won")
        game==True
    else:
        print('sorry try again')
        guess=int(input('please put in a number btwn 1 and 6'))
'''

"""
This function uses a while loop to print the Fibonacci series up to n.
  """

'''n=[0,1]
while(len(n)<10):
  sum=n[-1]+n[-2]
  n.append(sum)
  print(n)'''

'''def laughter():
    print("HAHA" * 3)
laughter()'''

'''fibon=[0,1]
def fibonacciSeries(fibon):
    while(len(fibon)<10):
        sum=fibon[-1]+fibon[-2]
        fibon.append(sum)
    return fibon
list1=[5,6]
print(fibonacciSeries(list1))'''
'''fruits=['banana','apples','chungwa','lemon']
a_fruits=[x for x in fruits if "a" in x]
print(a_fruits)

list1=[1,2,4,5,6,7,9,8,7,3,4,5]
#newlist=[]
#for item in iter(list1):
 #   newvalue= item * 2
 ##   newlist.append(newvalue)


newlist=[j*2 for j in list1]
print(newlist)'''

def divide(x,y):
    try:
        ans=x//y
        print("yes you can divide",ans)
    except Exception as e:
         print("the error is {e}")
print(divide (5,2))

    