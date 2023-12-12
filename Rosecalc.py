number1=int(input("Enter your first number "))
operator=(input("Enter your operator (+,-,*,//)"))
number2=int(input("Enter your second number "))

add=number1+number2
subtract=number1-number2
multiply=number1*number2
divide=number1//number2

if operator=="+":
    print(add)
elif operator=="-":
    print(subtract)
elif operator=="*":
    print(multiply)
elif operator=="//":
    print(divide)
else :
    print("invalid choice")
