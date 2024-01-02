def prime_num(num):
    prime_number=[]
    for i in range(1,num+1):
        if num%i==0:
            prime_number=prime_number.append(num)
            if len(prime_number)==2:
                print(f'(num)is a prime number')
            else:
                print(f'(num)is not a prime number')
prime_num(5)

    
