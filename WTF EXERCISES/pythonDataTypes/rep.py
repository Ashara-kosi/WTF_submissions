def rep1 (greet, nos_of_times):
    if nos_of_times <= 0:
      print(int(input("type in a number: ")))
    else:
      return greet * nos_of_times
greet = 'hello '
input_nos = int(input('Enter a number: '))
result = rep1(greet, input_nos)
print(result)
