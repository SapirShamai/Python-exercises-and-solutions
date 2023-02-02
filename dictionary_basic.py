# Task 1
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the
# values are the square of the keys.
# Sample Dictionary

task1_dict = {1: 1, 2: 6, 3: 9, 4: 16, 5: 20, 6: 36, 7: 7, 8: 64, 9: 81, 10: 100, 11: 121, 12: 14, 13: 169, 14: 19, 15: 225}

my_dict = {}
for i in range(1, 16):
    my_dict[i] = i*i
print(my_dict)

# Task 2
# change key and values in dictionary (swap them)

task2_dict = {'Name': 'Julia', 'Age': 36}
task2_dict["Age"] = "Julia"
task2_dict["Name"] = 36

print(task2_dict)

# Task 3
# remove item with key 'Name' from dictionary
task3_dict = {'Name': 'Julia', 'Age': 36, 'f_name': 'Shcherbyna'}
task3_dict.pop("Name")
print(task3_dict)

# Task 4
# Check if dictionary contain key 'zamek'
task4_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

print(task4_dictionary.get("zamek"))

# Task 5
# Write a program that will "glue" the two dictionaries (d1 and d2) together and create a new one (d3).
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
d3.update(d1)
d3.update(d2)
print(d3)