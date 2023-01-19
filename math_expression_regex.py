# Create a function that takes a string input and checks if it is a mathematical expression.
# Supported operators: +, -, *, /, % and only integers

import re

text = input("Enter your number here : ")
result = re.findall("\d+ ?[+*/%-] ?\d+", text)
if len(result) > 0:
    print(True)
else:
    print(False)