# Make any face happy. Create a function that takes a sentence containing sad faces and turn them into happy ones!
# This involves changing only the mouths.
# Make sure to only change the face if there are eyes before them.

import re

text = input("Enter your sad text : ")
result = re.sub(r" ?([8:;Xx])\(", r"\1)", text)
print("Happy face: ", result)