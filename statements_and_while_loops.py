# Task1:
# Your task is to write a Python program using while loop to print out numbers from -5 to 5, without 0. 
# You can't use break and continue statements!

my_numbers = ""
x = -6
while x < 5:
    x += 1
    if x == 0:
        continue
    my_numbers = my_numbers + str(x) + " "
print(my_numbers)

# Task2:
# Your task is to write a Python program using while loop, 
# that iterates over given string and converts the lower letters to capital letters and vice versa

my_text = str(input("Enter you text here: "))
result = ""
i = 0
while i < len(my_text):
    if my_text[i].islower():
        result += my_text[i].upper()
    elif my_text[i].isupper():
        result += my_text[i].lower()
    i += 1

print(result)

# Task3:
# Your task is to write a Python program using while loop, 
# to calculate the average of n integer numbers (input from the user). 
# Input 0 (zero) finishes entering numbers and prints out calculations.

print("Input few numbers to calculate their average: \nInput 0 to exit")
my_numbers = 0
my_count = 0

while True:
    number = int(input("Type a number: "))
    if number == 0:
        break
    my_count += 1
    my_numbers += number

if my_count > 0:
    print(f"Average of the above numbers is: {my_numbers / my_count}")
    

# Task 4:
# Your task is to write a Python program using while loop, to find indexes of prompted character in the given text.

my_str = str(input("Enter your text here:"))
my_letter = str(input("What should be found?: "))
i = 0
while i < len(my_str):
    if my_str[i] == my_letter:
        print(f"Character {my_letter} found at index {i}")
    i += 1


# Task5:
# Your task is to write a Python program using while loop,
# read (prompt) three numbers (a,b,c) and check how many numbers between a and b are divisible by c.
# Input 0 (zero) as a third number (divisor) finishes program and prints out the results.

while True:
    star_num = int(input("Type starting number: "))
    end_num = int(input("Type ending number: "))
    div_num = int(input("Type divisor: "))
    if div_num == 0:
        break
    else:
        for i in range(star_num, end_num+1):
            if i % div_num == 0:
                print(f"{i} is divisible by {div_num}")
            
    