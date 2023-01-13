# Task 1:
#7 mistake:


three_mul = 'fizz'    #1
five_mul = 'buzz'
num1 = 3
num2 = 5              #3
max_num = 100

for i in range(1, max_num):   #2
    if i % num1 == 0 and i % num2 == 0:         #5
        print(i, three_mul + five_mul)         #6
    elif i % num2 == 0:
        print(i, five_mul)
    elif i % num1 == 0:                       #4
        print(i, three_mul)


# Task 2 :
#
# Your task is to fix program non-working correctly. The problem:
# sum integers from 1 to 5 using while loop
# calculate what result should be and what you get after running the program

n = 5
number = 1
sum = 0
while number < n + 1:
    sum = sum + number
    number = number + 1
print("Sum =", sum)


# # Task 3 :
# Your task is to fix program non-working correctly. The problem:
# sum integers from 1 to 5 using range() function
# calculate what result should be and what you get after running the program

n = 6
sum = 0
for num in range(n):
    sum += num
print("Sum =", sum)

# # Task 4:
# Your task is to fix program non-working correctly. The problem:
# there are 4 short programs with loops, that should print some numbers, but they don't work at all!

# 1.
for x in range(3):
    print(x)

# 2.
for j in range(5):
    print("This is loop number ", j)

# 3.
x = 10
while x > 0:
    print(x)
    x -= 1

# 4.
countdown = 5
while countdown:
    print(f"{countdown}")
    countdown -= 1
else:
    print("Start!")


# Task 5 :
# Your task is to fix program non-working correctly. The problem:
# sum the three prompted integers
# however, if two values are equal sum should be zero
# calculate what result should be and what you get after running the program

x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x == y or y == z or x == z:
    result = 0
else:
    result = x + y + z
print("Calculated sum is ", result)


# Task 6 :
# sum the two prompted integers
# however, if the sum is between 15 to 20 (both numbers included) it should be calculated to 20
# calculate what result should be and what you get after running the program

x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y

if result >= 15 and result <= 20:
    result = 20

print("Calculated sum is : ", result)


# Task 7 :
# prompt two values and assign them to variables a and b
# write the Python program to swap these two variables
# calculate what result should be and what you get after running the program

a = input("First value: ")
b = input("Second value: ")

print("Before swapping: a =", a, " ,b = ", b)

temp = a
a = b
b = temp

print("After swapping: a =", a, " ,b =, ", b)


# Task 8 :
# prompt three float numbers and determine the largest and the smallest one
# calculate what result should be and what you get after running the program

x = float(input("First number: "))
y = float(input("Second number: "))
z = float(input("Third number: "))

print("The maximum value is ", max(x, y ,z))
print("The minimum value is ", min(x, y ,z))


# Task 9 :
# prompt value from the user and assign it to some variable
# if given value is 0 (zero) convert it to False and if given value is 1 convert it to True
# display results

x = input("Type your value: ")

if x == "0":
    x = False
elif x == "1":
    x = True
else:
    pass

print("Your entered value is now ", x)


# Task 10 :
# accept (prompt) two integers values from the user
# check whether a first number is divisible by second number and vice versa
# display results

x = int(input("First number: "))
y = int(input("Second number: "))

if x % y == 0:
    print("First number is divisible by second number, result =", x // y)
elif y % x == 0:
    print("Second number is divisible by first number, result =", y // x)
else:
    print("Numbers are non-divisable!")
