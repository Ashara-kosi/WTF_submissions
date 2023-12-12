def get_divisors_sum(number):
    divisors_sum = 1  # Start with 1 as all numbers are divisible by 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:  # Avoid counting squares twice
                divisors_sum += number // i
    return divisors_sum
 
def check_number_type(number):
    divisors_sum = get_divisors_sum(number)
    if divisors_sum < number:
        return 'Deficient'
    elif divisors_sum > number:
        return 'Abundant'
    else:
        return 'Perfect'
 
def classify_numbers(num):
    for i in range(2, num + 1):
        classification = check_number_type(i)
        print(f"{i} is {classification}")
        
        
input_number = int(input("Enter a number: "))
classify_numbers(input_number)
 