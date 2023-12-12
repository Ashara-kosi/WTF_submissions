#print("\ta\tb\tc")
#print("\\\\")
#print("'")
#print("\"\"\"")
#print("C:\nin\the downward spiral")
#print("'''")
#print('/\\//\\\\///\\\\\\')
#print('This quote is from \nIrish poet Oscar Wilde:\n\"Music makes one feel so romantic\n at least it always gets on one's nerve\n which is the same thing nowadays\"')#
      






#print(	9 // 5)
#print(695 % 20)
#print(7 + 6 * 5)
#print(7 * 6 + 5)
#print(248 % 100 / 5)
#print(6 * 3 - 9 / 4)
#print((5 - 7) * 4)
#print(6 + (18 % (17 - 12)))
# a=55
# b=100
# if a>b:
#     print('the first value is great')


# number =int(input('please put in the number'))

# if number%2==0:
#     print('this is an even number')

# else:
#     print('this is an odd number')



# for row in range(0,20):
#     for col in range(0,row+1):
#         print('*',end= " ")
#     print()


for num in range(1,13):
    print(f'Multiplication table for {num}')
    for j in range(1,13):
        ans = num * j
        print(f'{num} * {j}) ={ans}')