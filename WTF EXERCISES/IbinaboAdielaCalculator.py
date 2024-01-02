number_1 = int(input("type a number: "))
math_operator = input("type a math operator: ")
number_2 = int(input("type a second number: "))

if (math_operator == "+"):
    print(number_1 + number_2)
elif(math_operator == "-"):
    print(number_1 - number_2)
elif(math_operator == "/"):
    print(number_1 / number_2)
elif(math_operator == "*"):
    print(number_1 * number_2)
else:
    print("put a valid operator: ")
  
