# Task1:
# Your task is to write Python program that prints in one line all the numbers from 0 to 8 except 3 and 6

my_nums = ""
x = 0
while x < 9:
    if x == 3 or x == 6:
        x += 1
        continue
    else:
        my_nums += str(x) + " "
        x += 1
print(my_nums)

# Task2:
# Your task is to write Python program (using break statement), that prints:
# in first line the numbers from 0 to 7,
# in second line the numbers from 10 to 17,
# and in third line the numbers from 20 to 27.

list1 = []
list2 = []
list3 = []

for i in range(31):
    while i < 8:
        list1.append(i)
        break
    while 9 < i < 18:
        list2.append(i)
        break
    while 19 < i < 28:
        list3.append(i)
        break
        

print(" ".join(map(str, list1)))
print(" ".join(map(str, list2)))
print(" ".join(map(str, list3)))

# or: another way:

for i in range(3):
    for j in range(i*10, i*10 + 10):
        print(j, end=" ")
        if j == (i+1)*10 - 3:
            break
    print()
 
# Task 3:
# Your task is to write Python program (using continue and break statements), that reads (prompts) two integers.
# If first number is smaller than second number, then find all numbers between them that are divisible by 3 and print them out.
# Use continue statement!
# If first number is bigger than second number, then find first number between them that is divisible by 5 and print it out.
# Start iterating from bigger number and use break statement!
# If numbers are equal only print that information!


while True:
    first_num = int(input("First number: "))
    second_num = int(input("Second number: "))
    if first_num < second_num:
        for i in range(first_num, second_num+1):
            if i % 3 == 0:
                print(f"{i} is divisible by 3.")
            else:
                continue
    elif first_num > second_num:
        for i in range(first_num, second_num+1, -1):
            if i % 5 == 0:
                print(f"{i} is divisible by 5")
                break
    else:
        print("Numbers are equal!")


# Task4:
# Your task is to write Python program (using continue and break statements), that reads (prompts) two integers.
# First integer must be bigger than 100 and must be odd!
# Second integer must be odd!
# If first number is divisible by second number, then you'll get one "point" (some variable increases by 1) and you can continue typing numbers. Use continue statement!
# If first number is not divisible by second number, then you'll quit the game. Use break statement!
# Print out information about points!

points = 0
x = 0
while x < 2:

    first_num = int(input("First number: "))
    if first_num < 100 or first_num % 2 == 0:
        print("First number must be bigger than 100 and odd, try again!")
        break

    second_num = int(input("Second number: "))
    if second_num % 2 == 0:
        print("Second number must be odd, try again!")
        break

    if first_num % second_num == 0:
        print("You earned a point!")
        points += 1
        continue
    else:
        print("You've made a mistake!")
        break

print(f"You gathered {points} point(s)!")

# Task5:
# Your task is to write a Python program using loop, that iterates over the entered string and counts sum of the digits in the string.
# User should be prompted to enter her/his characters with the keyboard, even without looking at it.
# Store the information about sum of the digits.
# Program should terminate after encountering '=' character in the string (if it is present there).


x = True
while x:
    my_sum = 0
    my_string = input("Enter your characters here: ")
    for i in my_string:
        if i.isdigit():
            print(f"Found a digit {i}")
            my_sum += int(i)
        elif i == "=":
            print("Exit after '=' sign")
            x = False
            break

    print(f"Sum of digits: {my_sum}")
