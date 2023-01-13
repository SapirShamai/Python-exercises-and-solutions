# # task 1
# Your task is to write a program which asks the user three times for a number.
# If number is even print ‘Even number’, else print ‘Odd number’.
x = 1
while x <= 3:
    x += 1
    number = int(input("Enter number : "))
    if number % 2 == 0:
        print("number is even")
    else:
        print("number is odd")

# # task 2
##Your task is to write a program which asks the user about number of arguments in range() function.
# If number is 1 ,program asks for another number and then prints digits from range() function with given number.
# If number is 2 ,program asks for two numbers and then prints digits from range() function with given range.
# If number is 3 ,program asks for three numbers and then prints digits from range() function with given range and given step.


number = int(input("Enter number of arguments in range () function : "))

if number == 1:
    stop = int(input("Enter stopping number : "))
    for i in range(stop):
        print(i)

elif number == 2:
    start = int(input("Enter starting number : "))
    stop = int(input("Enter stopping number : "))
    for i in range(start, stop):
        print(i)

elif number == 3:
    start = int(input("Enter starting number : "))
    stop = int(input("Enter stopping number : "))
    step = int(input("Enter step number : "))
    for i in range(start, stop, step):
        print(i)
else:
    print("Sorry but you must enter a number between 1-3 ")

# #task 3
#Your task is to write a program which prints all the divisors of a number. The number comes from the user's input.

i = 0
number = int(input("Enter a number : "))
for i in range(number + 1):
    if number % (i+1) == 0:
        print(i+1)

# #task 4
# #Your task is to write a program to check if input number is a prime number.

number = int(input("Enter a number :"))
if 1 >= number:
    print("Number is not prime")
elif number == 2:
    print("2 is a prime number")
else:
    for i in range(2, number):
        if number % i == 0:
            print(str(number) + " is nottt a prime number")
            break
        else:
            print(str(number) + " is a prime number")
            break

# #task 5
# #Your task is to write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)

# task 6
#Your task is to write a program to print all the numbers between 1000 and 2000 which are divisible by 7 but are not a multiple of 5.

for num in range(1000, 2001):
    if num % 7 == 0 and num % 5 != 0:
        print(num)
