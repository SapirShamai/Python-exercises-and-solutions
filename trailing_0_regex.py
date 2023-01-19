# Create a function that takes a string input as a number and replaces leading and trailing zeros.

import re
text = input("Enter your text here : ")
result = re.sub("^0+|0+$", "", text)
print(result)