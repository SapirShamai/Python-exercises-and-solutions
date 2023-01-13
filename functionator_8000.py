# Functioninator 8000
# Task
# Create a function that takes a single word string and does the following:
# Concatenates inator to the end if the word ends with a consonant otherwise, concatenate -inator instead.
# Adds the word length of the original word to the end, supplied with '000'.


y = 0
while y == 0:
    x = input("Enter a word here :")
    if " " in x:
        print("no spaces please...try again")
    else:
        y += 1

if x[-1] == "a" or x[-1] == "i" or x[-1] == "e" or x[-1] == "o" or x[-1] == "u" or x[-1] == "y":
    new_x = x + "-inator"
    print(new_x + " " + str(len(x)) + "000")
else:
    new_x = x + "inator"
    print(new_x + " " + str(len(x)) + "000")