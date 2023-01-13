# Task
# Write a program that detects if a string has an even/odd number of characters and prints "even" or "odd" accordingly.

text = input("Enter your text here: ")
if len(text) % 2 == 0:
    print("The number of characters is even")
else:
    print("The number of characters is odd")