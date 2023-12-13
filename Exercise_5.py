# Question 1

# num = int(input("please enter a number to check: "))
# result = 0
# for i in range(1, num):
#     if(num%i) == 0: 
#         result = result + i
# if result == num:
#     print(num, "is perfect")
# else:
#     print(num, "is not perfect")

# Question 2

# num = int(input("what is the upper number for the range: 29 "))
# result = 0
# for i in range(1, 30):
#     if(num%i) == 0: 
#         result = result + i
# if result == num:
#     print(num, "is perfect")
#     print(num, "is deficient")
#     print( num, "is abundant")

# def classify_number(num):
#     if num <= 0:
#         return "Please enter a positive integer."

#     # Find divisors and calculate their sum
#     divisors_sum = sum([i for i in range(1, num) if num % i == 0])

#     # Classify the number
#     if divisors_sum == num:
#         return "Perfect"
#     elif divisors_sum < num:
#         return "Deficient"
#     else:
#         return "Abundant"

# # Get user input
# try:
#     number = int(input("Enter a positive integer: "))
#     result = classify_number(number)
#     print(f"{number} is a {result} number.")
# except ValueError:
#     print("Please enter a valid integer.")


# def classify_numbers(start, end):
#     if start <= 0 or end <= 0 or start > end:
#         return "Please enter valid positive integers for the range."

#     results = {}
#     for num in range(start, end + 1):
#         divisors_sum = sum([i for i in range(1, num) if num % i == 0])

#         if divisors_sum == num:
#             results[num] = "Perfect"
#         elif divisors_sum < num:
#             results[num] = "Deficient"
#         else:
#             results[num] = "Abundant"

#     return results

# # Get user input for the range
# try:
#     start_range = int(input("Enter the start of the range (positive integer): "))
#     end_range = int(input("Enter the end of the range (positive integer): "))

#     results_dict = classify_numbers(start_range, end_range)

#     # Print results
#     for num, result in results_dict.items():
#         print(f"{num} is a {result} number.")
# except ValueError:
#     print("Please enter valid integers for the range.")


# Question 2
# A perfect integer is a positive integer that is equal to the sum of its proper divisors. Proper divisors of a number are all positive divisors excluding the number itself.

# A deficient integer is a positive integer for which the sum of its proper divisors is less than the number itself.

# An abundant integer is a positive integer for which the sum of its proper divisors is greater than the number itself.

# def classify_numbers(start, end):
#     results = {}
#     for num in range(start, end + 1):
#         divisors_sum = sum([i for i in range(1, num) if num % i == 0])

#         if divisors_sum == num:
#             results[num] = "Perfect"
#         elif divisors_sum < num:
#             results[num] = "Deficient"
#         else:
#             results[num] = "Abundant"

#     return results

# # Define the range
# start_range = 2
# end_range = 29  # You can adjust the end value as needed

# results_dict = classify_numbers(start_range, end_range)

# # Print results
# for num, result in results_dict.items():
#     print(f"{num} is a {result} number.")


# Question 3

# import random

# def hi_low_game():
#     # Generate a random number between 0 and 100
#     secret_number = random.randint(0, 100)

#     print("Welcome to the Hi-Low Number Guessing Game!")
#     print("Try to guess the secret number between 0 and 100.")

#     while True:
#         # Get user input for a guess
#         user_guess = input("Enter your guess (or type 'exit' to quit): ")

#         # Check if the user wants to exit
#         if user_guess.lower() == 'exit':
#             print(f"The secret number was {secret_number}. Thanks for playing!")
#             break

#         try:
#             # Convert the user's input to an integer
#             user_guess = int(user_guess)

#             # Check if the guess is within the valid range
#             if 0 <= user_guess <= 100:
#                 # Provide hints and check if the guess is correct
#                 if user_guess < secret_number:
#                     print("Too low! Try a higher number.")
#                 elif user_guess > secret_number:
#                     print("Too high! Try a lower number.")
#                 else:
#                     print(f"Congratulations! You guessed the correct number {secret_number}.")
#                     break
#             else:
#                 print("Please enter a number within the range of 0-100.")

#         except ValueError:
#             print("Invalid input. Please enter a valid number or 'exit' to quit.")

# # Start the game
# hi_low_game()


# Question 4
# def hailstone_sequence(n):
#     sequence = [n]

#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1

#         sequence.append(n)

#     return sequence

# # Get user input for the initial number
# try:
#     initial_number = int(input("Enter the initial number for the hailstone sequence: "))
#     if initial_number > 0:
#         result_sequence = hailstone_sequence(initial_number)
#         print(f"The hailstone sequence for {initial_number} is: {result_sequence}")
#     else:
#         print("Please enter a positive integer.")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")

print("hello world!")