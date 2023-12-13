import random
#Question 1.
def check_number(user_input):
    divisors = []
    for i in range(1,user_input):
        if user_input % i == 0:
            divisors.append(i)
    divisors_sum = sum(divisors)

    if divisors_sum == user_input:
        result = "This is a perfect number"
    elif divisors_sum > user_input:
        result = 'This is an abundant number'
    else:
        result = 'This is a deficient number'
    return result
user_input = int(input('Enter a number: '))
print(check_number(user_input))


#Question 2.
# def check_number(user_input):
#     divisors = []
#     for i in range(1,user_input):
#         if user_input % i == 0:
#             divisors.append(i)
#     divisors_sum = sum(divisors)
#     if divisors_sum == user_input:
#         result = f"{user_input} is a perfect number"
#     elif divisors_sum > user_input:
#         result = f"{user_input} is an abundant number"
#     else:
#         result = f"{user_input} is a deficient number"
#     return result
# user_input = int(input('What is the number for the upper range: '))
# for i in range(1, user_input+1):
#     print(check_number(i))


#Question 3.
# def hi_low():
#     computer_guess = random.randint(0,100)
#     user_guess = 1000
#     while user_guess != computer_guess:
#         user_guess = int(input('Enter a number: '))
#         if user_guess < 0 or user_guess > 100:
#             break
#         else:
#             if user_guess < computer_guess:
#                 print('Guess higher')
#             elif user_guess > computer_guess:
#                 print('Guess lower')
#             else: 
#                 print('Congratulations, You guessed correctly')
# hi_low()


#Question 4.
# def hailstone_sequence(user_input):
#     sequence_list = [user_input]
        
#     while user_input != 1:
#         if user_input % 2 == 0:
#             new_number = user_input / 2
#             sequence_list.append(new_number)
#         else:
#             new_number = (user_input * 3) + 1
#             sequence_list.append(new_number)

#         user_input = new_number

#     return sequence_list

# user_input = int(input('Enter a number to generate hailstone sequence: '))

# print(hailstone_sequence(user_input))


#Name of Group Members
# Folayemi Oladotun
# Fatima Animashaun
# Peace Adamson
# Chidera Mba
# Titilayo Dada
# Nancy Dzikunu-Bansah
# Ezinne Uche
# Ibinabo Adiela
# Uduak Njoku



