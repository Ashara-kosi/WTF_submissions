import math

# Number 1

# +----+
# \    /
# /    \
# \    /
# /    \
# \    /
# /    \
# +----+

characters = ["+----+", "\    /", "/    \\", "\    /", "/    \\","\    /", "/    \\", "+----+"]
for i in characters:
    print(i)

# Number 2

# **********
# **********
# **********
# **********
# **********

# for i in range(5):
#     for j in range(10):
#         print("*", end=" ")
#     print()

# Number 3
# a
# for i in range(1, 7):
#     print(i)

# b
#  range(start, stop, step)
# for j in range(2, 13, 2):
#     print(j)

# c
# for k in range(4, 80, 15):
#     print(k)

# d
# for l in range(30, -21, -10):
#     print(l)

# e
# for m in range(-7, 14, 4):
#     print(m)

# f

# g

# Number 4
# 1
# 22
# 333
# 4444
# 55555
# 666666

# for i in range(7):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# Number 5
# def pay(salary, no_hours):
#     if no_hours > 8:
#         overtime = 1.5 * salary
#         money = (salary * no_hours) + overtime
#     else:
#         money = salary * no_hours
#     return money

# TA_salary = float(input("Enter salary: "))
# TA_hours = int(input("Enter hours: "))

# payment = pay(TA_salary, TA_hours)
# print(f"The money to be paid is: {payment}")

# Number 6
# Function that calculates the area of a circle
# print(math.pi)

# def area_of_circle(radius):
#     area = math.pi * radius ** 2
#     return area

# radius = float(input("Enter radius: "))
# circle_area = area_of_circle(radius)
# print(f"{circle_area:.2f}")