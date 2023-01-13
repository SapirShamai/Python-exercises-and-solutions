# Task 1 :
# Your task is to write a program which asks the user three times about two integer numbers to compare.
# Use both comparison and logical operators, for example use logical comparison between two or more comparion operators:

x = 0
while x < 3:
    first = int(input("Enter first number : "))
    second = int(input("Enter second number : "))
    if first == second:
        print("Numbers are equal")
    elif first > second:
        print("First number is bigger then than the second number")
    elif first < second:
        print("Second number is bigger than the first number")
    x += 1


x = 0
while x < 3:
    first = int(input("Enter first number : "))
    second = int(input("Enter second number : "))
    if first % 2 == 0 and second % 2 == 0:
        print("Both numbers are even")
    elif first % 2 == 0 and second % 2 != 0:
        print("First number is even and the second number is odd")
    elif first % 2 != 0 and second % 2 == 0 :
        print("Second number is even and first number is odd")
    else:
        print("Both numbers are odd")
    x += 1

# Task 2 :
# Your task is to write a Python program to convert month name to a number of days.
#User should be prompted to enter name of the month and the output shoul be the number of days in given month.

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(months)
month = input("Enter a month : ")
if month == "January" or month == "March" or month == "May" or month == "July" or month == "October" or month == "December":
    print("There are 31 days on this month")
elif month == "February":
    print("28 days and 29 in every fourth year")
else:
    print("There are 30 days on this month")
