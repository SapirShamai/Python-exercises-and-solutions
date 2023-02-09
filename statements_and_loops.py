# Task1:
# Your task is to write a Python program to create the multiplication table (from 1 to 10) of a number. 
# Number is prompted by the user.

number = int(input("Please enter number: "))
for i in range(1,11):
    print(f"{number} X {i} = {number*i}")

# Task 2:
# Your task is to write a Python program to construct the following pattern, using a for loop.

for i in range(1, 10):
    print(str(i) * i)

# Task3:
# Your task is to write a Python program that accepts a word from the user and reverses it, using a for loop.

my_string = str(input("Input a word to reverse: "))
reversed_string = []
for i in my_string[::-1]:
    reversed_string += i
print("Reversed word: ", "".join(reversed_string))

# Task4:
# Your task is to write a Python program using for loop,
# that iterates over given string and changes every ocurence of 'o' letter into big letter 'O'.
# for example: "Hello, I love you, won't you tell me your name?"

my_text = str(input("Please enter your text here: "))
my_new_text = []
for i in my_text:
    if i == "o":
        i = "O"
    my_new_text += i

print("".join(my_new_text))

# Task5:
# Your task is to write a Python program using for loop, that counts digits and letters.
# User should be prompted to enter her/his characters with the keyboard, even without looking at it.
# Store the information about number of digits and letters in some variables.

my_characters = input("Enter your characters: ")
digit_count = 0
letter_count = 0
other_characters = 0

for i in my_characters:
    if i.isdigit():
        digit_count += 1
    elif i.isalpha():
        letter_count += 1
    else:
        other_characters += 1
        

print(f"Number of digits: {digit_count}\nNumber of letters: {letter_count}")