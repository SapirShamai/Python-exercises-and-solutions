#
## String Basics 2

#Task 1:
#Create a variable called text to store the data: Berlin is a world city of culture, politics, media and science. . Your task is to print the length of the text variable on the screen.


text = "Berlin is a world city of culture, politics, media and science."
print(len(text))

#Task 2:
#Reuse the variable called text and print the first and the last characters on the screen.
print(text[0], text[-1])

#Task 3:
#Reuse the variable called text and print the first three characters in upper case.
x = text.upper()[0:3]
print(x)

#Task 4:
# Create the variable called text with the following content: Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital , then count how many times the letter B  appears in the text.
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital "
print("B appears :", text.count("B"), "times")

#Task 5:
#Create a variable called text to store the data: Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau. . Your task is to print the last 10 characters of the text variable on screen.
text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
x = text[-10:]
print(x)

#Task 6 :
#Create a variable called text to store the data: ---Python programming--- . Your task is to remove the hyphen (-) character from the string.
text = "---Python programming---"
print(text[3:-3])

#Task 7 :
#Create two variables to store your first and your last name. Your task is to concatenate the two variables using the appropriate labels.
first = "Sapir"
last = "Shamai"
print("Firstname: " + first + "\nLastname: " + last)