# Task1:
#Create a recursive function named countdown with a single integer input
# argument that prints a countdown starting from the given number.

def countdown(my_number):
    number = int(my_number)
    for i in range(number, 0, -1):   # counting from number to 0 but not including 0
        print(i)
    return 0

print(countdown(5))

# Task2:
# Create a recursive function named factorial that returns the factorial of a number
# (the number multiplied by every integer lower than the number and greater than 0).
# example: factorial 10 = print(10*9*8*7*6*5*4*3*2*1)

def factorial(my_num):
    number = int(my_num)
    my_sum = 1
    for i in range(1, number+1):
        my_sum = my_sum * i
    return my_sum

print(factorial(10))

# Task3:
# Create a function called harmonic_sum that requires an integer as an argument.
# The function will return the harmonic sum of the integer.
# The harmonic sum is the sum of reciprocals of the positive integers. The harmonical sum of 2 is:
# 1/1 + 1/2 = 1.5

def harmonic_sum(number):
    my_number = int(number)
    result = 0
    for i in range(1,my_number+1):
        result += (1/i)
    return result

print(harmonic_sum(4))