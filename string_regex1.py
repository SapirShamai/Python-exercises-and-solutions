import re
# Task 1 :
# Create a variable called text to store the data:
# Berlin is a world city of culture, politics, media and science.
# Then search for the first white space character in the string and print its location using the appropriate label.

text = "Berlin is a world city of culture, politics, media and science. "
result = re.search("\s", text)
print("The first white space character is located at position: ", result.start())

# Task 2 :
# Create a variable called text to store the data:
# Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital.
# Then search for the word Frankfurt in the string .

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital. "
result = re.search("Frankfurt", text)
print(result)

# Task 3
# Create a variable called text to store the data:
# Berlin is a city of culture.
# Replace the spaces with a hyphen.

text = "Berlin is a city of culture."
result = re.sub(" ", "-", text)
print(result)

# Task 4 :
# Create a variable called text to store the data:
# Berlin is a city of culture.
# Search if the phrase "in" appears inside the string. Print the output of the regex function.

text = "Berlin is a city of culture."
result = re.search("in", text)
print(result)

# Task 5 :
# Use the text variable from the previous task.
# Create a regular expression to look for any word that starts with an upper case "B".
# Print the position (start- and end-position) of the first match occurrence.

text = "Berlin is a city of culture."
result = re.search("B\w+", text)
print(result.span())

# Task 6
# Create a variable called text to store the data:
# The rain in Spain.
# Count how many times the subphrase "ai" appears in the string. Print the results on the screen.

text = "The rain in Spain."
result = len(re.findall("ai", text))
print(result)


