# Task 1
# Create a variable called fruits and one after another add the elements Apples, Cherries and Strawberries.
# Loop over the list fruits and print every element to the screen.

fruits = []
fruits.append("Apples")
fruits.append("Cherries")
fruits.append("Strawberries")
for i in fruits:
    print(i)

# Task 2
# Create a variable cities which holds a list with the cities London, Paris, Berlin and Amsterdam.
# Print the sentence The capital city of Germany is: Berlin to the screen, using the string Berlin from the cities array.

cities = ["London", "Paris", "Berlin", "Amsterdam"]
print(f"The capital city of Germany is: {cities[2]}")

# Task 3
# Store the colors cyan, magenta, green, yellow, black and white in a list called colors.
# Remove the colors green and white. Print the remaining colors to the screen.

colors = ["cyan", "magenta", "green", "yellow", "black", " white"]
colors.remove("green")
colors.pop(4)
for i in colors:
    print(i)

# Task 4
# Store the letters p, e, n, g, u, i, n in a list.
# Combine those letters into a single string penguin.
# Capitalize that string and print it to the screen.

my_list = ["p", "e", "n", "g", "u", "i", "n"]
my_string = "".join(my_list)
print(my_string.capitalize())