# Exercise 1: Reverse the tuple
tuple1 = (10, 20, 30, 40, 50)
# Expected output:
# (50, 40, 30, 20, 10)
print(tuple1[::-1])

# Exercise 2: Access value 20 from the tuple
tuple2 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple2[1][1])

# Exercise 3: Create a tuple with single item 50
my_tuple = tuple("50")
print(type(my_tuple))

# Exercise 4: Unpack the tuple into 4 variables
tuple3 = (10, 20, 30, 40)
# Your code
# print(a) # should print 10
# print(b) # should print 20
# print(c) # should print 30
# print(d) # should print 40
a = tuple3[0]
b = tuple3[1]
c = tuple3[2]
d = tuple3[3]
print(a, b, c, d)


# Exercise 5: Swap two tuples in Python
tuple_1 = (11, 22)
tuple_2 = (99, 88)
# Expected output:
# tuple1: (99, 88)
# tuple2: (11, 22)

tuple_1, tuple_2 = tuple_2, tuple_1

print(tuple_1, tuple_2)

# Exercise 6: Modify the tuple
# Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
tuple6 = (11, [22, 33], 44, 55)
# Expected output:
# tuple1: (11, [222, 33], 44, 55)
tuple6[1][0] = 222
print(tuple6)

# Exercise 7:
# Write a Python function that takes two lists and returns True if they have at least one common item.
def check_lists(list1: list, list2: list) -> bool:
    x = set(my_list).intersection(set(my_list1))
    #print(bool())
    return bool(x)


my_list = ["sapir", "shamai", "hello"]
my_list1 = ["hello", "world"]
print(check_lists(my_list, my_list1))

my_list = ["sapir", "shamai"]
my_list1 = ["hello", "world"]
print(check_lists(my_list, my_list1))

# Exercise 8:
# Write a Python function to insert a given string at the beginning of all items in a list.
#Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
# NOTE: Items in given string can be str, int, float NOT list, tuple, set or dictionary


def insert_to_list(my_list, my_string):
    my_nea_list = []
    for i in my_list:
        i = my_string + str(i)
        my_nea_list.append(i)
    return my_nea_list



new_list = [1, 2, 3, 4]
new_str = "emp"
print(insert_to_list(new_list, new_str))