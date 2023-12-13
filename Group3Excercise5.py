#Question 1
def is_perfect_number(n):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i

    return sum_of_divisors == n
 
# Example usage
number = int(input("Please enter a number to check: "))
 
if is_perfect_number(number):
  print(f"{number} is a perfect number.")
else:
  print(f"{number} is not a perfect number.")

print() #This empty print statement when executed, leaves a line after each question in the terminal for a clearer code

#Question 2
def classify_number(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    
    if divisors_sum == num:
        return "Perfect"
    elif divisors_sum < num:
        return "Deficient"
    else:
        return "Abundant"

# Test cases
numbers = int(input("What is the upper number for the range: "))
for number in range(numbers + 1):
    category = classify_number(number)
    print(f"{number} is {category}")

print()

#Question 3
import random

def hi_low_game():
    hidden_number = random.randint(0, 100)
    max_attempts = 5  

    print("Welcome to the Hi-Low Number Guessing Game! \nTry to guess the hidden number between 0 and 100.\nf'You have {max_attempts} attempts.")
    
    for attempt in range(max_attempts):
        guess = int(input("Enter your guess: "))
        
        if guess == hidden_number:
            print("Congratulations! You guessed the number correctly!")
            break
        elif guess < 0 or guess > 100:
            print("Quitting the game.")
            break
        elif guess < hidden_number:
            print("Go higher.")
        else:
            print("Go lower.")
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The hidden number was {hidden_number}.")

# Start the game
hi_low_game()

print()

#QUESTION 4
def hailstone_sequence(n):
  sequence = [n]
  while n != 1:
    if n % 2 == 0:
      n //= 2
    else:
      n = 3 * n + 1
    sequence.append(n)
  return sequence

# Example 
starting_number = int(input("Enter a number to start the hailstone sequence: "))
sequence = hailstone_sequence(starting_number)
 
print(f"Hailstone sequence for {starting_number}: {sequence}")