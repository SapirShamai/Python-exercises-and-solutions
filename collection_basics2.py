# Task 1
# Create a variable called person which should hold a dictionary.
# The dictionary should have the key name with the value Bart Simpson and the key address with the value 742 Evergreen Terrace.
# Print the name and the address separated by comma to the screen.
person = {
     "name": "Bart Simpson",
     "aadress": "742 Evergreen"
}
print(person["name"] + ", " + person["aadress"])

# Task 2
#Create two variables one called bart and the other called homer.
# Each stores a dictionary, one with the key name and the value Bart Simpson, the other one with the same key but the value Homer Simpson.
# Create a third variable address with a dictionary which only has one key address.
# Use update to add the address to both bart and homer. Print bart['address'] to the screen.

bart = {"name": "Bart Simpson"}
homer = {"name": "Homer Simpson"}
address ={"address": "742 Evergreen"}
bart.update(address)
homer.update(address)
print(bart["address"])

# Task 3
# Create a variable ages which holds a dictionary with the key Peter and the value 36, the key Robin and the value 29 and the key Michael with the value 33.
# Loop over the dictionary and print the name with the age.

ages ={
     "Peter": 36,
     "Robin": 29,
     "Michael": 33
}
for name, age in ages.items():
     print(name,":", age)

# Task 4
# Store the animals Alligator, Tiger, Parrot, Hamster, and Dolphin as keys in a dict. Use random numbers as values.
# Now remove all keys ending with r from the dictionary and print the resulting dict to the screen.
my_dict = {
     "Alligator": 88,
     "Tiger": 78,
     "Parrot": 23,
     "Hamster": 65,
     "Dolphin": 5
}
my_dict.pop("Alligator")
my_dict.pop("Tiger")
my_dict.pop("Hamster")
print(my_dict)