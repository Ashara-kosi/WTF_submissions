#print('my\tname\tis\bOnyinye')
#print("\ta\tb\tc")
#print("\\\\")
#print("'")
#print("\"\"\"")
#print("c:\nin\the download spiral")
#print("/ \\ // \\\\ /// \\\\\\")
#print("This quote is from \n Irish poet Oscar Wilde:")
#print("\"Music makes one feel so romantic \n - at least it always gets on one's nerves-\n which is the same thing nowadays.\"")
#print("A \"quoted\" String is \n\'much\' better if you learn \nthe rules of \"escape sequences.\"")
#print("Also, \"\" represents an empty String.\nDon't forget: use \\ \" instead of \" !\n\'\' is not the same as\"")
#print(9/5)
#print(695 % 20)
#print(7 + 6 * 5)
#print(7 * 6 + 5)
#print(248 % 100 / 5)
#print(6 * 3 - 9 / 4)
#print((5 - 7) * 4)
#print(6 + (18 % (17 - 12)))
#string_variable ="Monty python"
#first_character =string_variable[0]
#print(first_character)
#string_variable ="Monty python"
#print(string_variable[-1])

#string_variable ="Monty python"
#print(string_variable[len(string_variable)-1])
#string_variable ="Monty python"
#print(string_variable[:5 ])
#string_variable ="homebody"
#print(string_variable[:4])
#string_variable ="homebody"
#print(string_variable[4:]) 

# s = "abcdefghij"
# first_half =s[:len(s)//2]
# print("First Half:", first_half)
# second_half = s[len(s)//2:]
# print("Second Half:", second_half)

# s = "abcdefghijk"
# middle_character = s[len(s)//2]
# print ("middle_character:",middle_character)
# first_half =s[:len(s)//2]
# print("first_half:",first_half)
# second_half = s[len(s)//2+1:]
# print("second_half:",second_half)

# x = 'water'
# result = x.replace('w','c',1)
# print(result)

# S = "what is your name?"
# result_a = S[::2]
# print(result_a)

# n = int(input("Enter number: "))
# x = 0  # important declaration..   
# for i in range(1, n +1):
#     if i * (i + 1)== n:
#          print("is pronic")
#     else:
#          print( "not pronic")
               
# n = int(input("Enter number: "))
# x = 0  # important declaration..
# for i in range(1, n + 1):
#    if i * (i + 1) == n:
#        print(True)
#    else:
#        print(False)  

         

# def is_pronic(num):
#     pronic=False
#     for i in range(1,1000):
#         if ((i*(i+1))==num):
#             pronic=True
#             print(f"the {num} number is is divisble by {i} and {i+1}")
#             break
#              #return True
#         return pronic,i,i+1
# num=int(input('enter your number:'))

# print(is_pronic(num))
#     '''12if is_pronic:
#     print("yes")





# # for row in range(0,10):
# #     for col in range(0,row+1):
# #         print('*',end="")
# #     print()


# for num in range(1,11):
#     print(f'mutiplication table for{num}')
#     for k in range(1,11):
#         ans = num * k
#         print(f'{num} * {k} = {ans}')


# def draw_pattern():
#     print("+----+")
#     for _ in range(4):
#         print("\\ /")
#         print("/ \\")
#     print("\\ /")
#     print("/ \\")
#     print("+----+")
# # Call the function to produce the output
# draw_pattern()

# Using a for loop along with an if statement to filter and create new list 'x'
# fruits =('banana','mango','apple','orange','lime')
# x = []

# for fruit in fruits:
#     if 'a' in fruit:
#         x.append(fruit)
#     print(x)

#      = [x for x in a_fruitsfruits if 'a' in x]
#     print(a_fruits)

# list1 = [2,4,5,6,7,8,9,0,1,2,4]
#             #    newlist basket
# newlist = [] 
#             # let's go through each num in the original list
# for item in list1:
#             #  double the num
#     newvalue = item * 2
#             # Add the doubled num to the new list
#     newlist.append(newvalue)
#             # print the new list
# print(newlist)
# # usinglist comprehension to double each num and create a new list
# newlist = [j * 2 for j in list1]
# print(newlist)

# fruits = ["Date", "Guava", "Pineapple", "Soursop", "Orange"]
# newlist =[fruit for fruit in fruits if 'e'in fruit ]
# print(newlist)

# list1 = [2,4,5,6,7,8,9,0,1,2,4]
# newlist = [j * 2 for j in list1]
# print(newlist)

# def divide(a,b):
#     try:
#         result = a // b
#         print("yeah you right :", result)
# Exception as e is used when you don't know what the error is.
#     except Exception as e :
#         print("sorry ! it can't work")

# divide(5,10)
# print(divide(5,0))
# why am i having the same answer

def divide(a,b):
    try:
        result = a // b
        print(f'your answer is (ans)')
# Exception as e is used when you don't know what the error is.
    except Exception as e :
        print(f'The error is (e)')

divide(5,10)
print(divide(5,0))