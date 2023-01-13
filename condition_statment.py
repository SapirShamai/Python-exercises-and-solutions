# Task 1 :
#Your task is to write a Python program to calculate the sum of three integers given (prompted) by user.
#If the values are equal then calculate triple value of their sum.
#Print out an appropriate message to the user.

first_num = int(input("First number : "))
second_num = int(input("Second number : "))
third_num = int(input("Third number : "))

sum1= (first_num + second_num +third_num) * 3
sum2= first_num + second_num +third_num

if first_num == second_num == third_num:
    print("The triple sum is : ", sum1)
else:
    print("The sum is : ", sum2)

# Task 2 :
#Your task is to write a Python program to get the difference between a two given numbers (prompted by user).
#If the first number is greater than second then calculate double difference between numbers.
#Otherwise calculate the absolute difference between numbers.
#Print out an appropriate message to the user.

first_num = int(input("First number : "))
second_num = int(input("Second number :"))

if first_num > second_num:
    print("The result is double the difference : ",(first_num - second_num) * 2)
elif first_num < second_num:
    print("The result is the absolute difference : ",abs(second_num - first_num))
else:
    print("The result is : ", first_num - second_num)

# Task 3 :
#Your task is to write a Python program to find whether a given number (prompted from the user) is even or odd. Print out an appropriate message to the user.

num = int(input("Please enter a number : "))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Task 4 :
#Your task is to write a Python program which accepts (prompts) the float radius of a circle from the user and compute its area.
#Round the result to two decimals!
#Print out an appropriate message to the user.

import math

radius = float(input("Enter the radius of the circle : "))
d = radius * 2
a = math.pi * radius ** 2
print("The area of the circle with radius ", radius,"and diameter : ", d, "is : ", a)

# Task 5 :
#Your task is to write a Python program to guess a number between 1 to 9.
#User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct,
# #on successful guess, user will get a "Well guessed!" message, and the program will exit.

num = 0
while num != 5:
    num = int(input("Guess a number between 1 and 10 until you get it right : "))
    if num < 1 or num > 10:
        print("I accept only numbers between 1 and 10, try again ")
print("Well guessed!!")

# Task 6 :
#Your task is to write a Python program to convert temperatures to and from Celsius, Fahrenheit.
#In the centigrade scale, which is also called the Celsius scale, water freezes at 0 degrees and boils at 100 degrees.
#In the Fahrenheit scale, water freezes at 32 degrees and boils at 212 degrees.


# first I found formula examples:     (10 c * 1.8)+32          (90 f -32) / 1.8

scale = input("Input the scale you would like to convert (F/C) : ")
num = float(input("Input the value of temperature you would like to convert : "))

if scale == "C":
    print(num, scale, "equals to : ", (num * 1.8) + 32, "F")
elif scale == "F":
    print(num, scale, "equals to : ", (num - 32) / 1.8, "C")
else:
    print("Please enter the right scale")

# Task 7 :
#Your task is to write a Python program to construct the following pattern. Upper part should be done in one line of code without using a loop.
#Lower part can be done with any kind of loop or also with one line of code and without loops.

x = "* "
print(x, x*2, x*3, x*4, x*5, sep="\n")
print(x*4, x*3, x*2, x, sep="\n")

# Task 8:
#Your task is to write a Python program to get the Fibonacci series between 0 to 50.
#Note: The Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it.

n1, n2 = 0, 1

while n1 + n2 < 50:
    count = n1 + n2
    print(count)
    n1 = n2
    n2 = count


