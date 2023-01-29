# # Task1:
# # Create two simple functions isOdd and isEven that each take a single Integer
# # and return a Boolean indicating whether the passed value is odd or is even.
#
# def isEven(num):
#     # this function checks if a number is even
#     result = num % 2 == 0
#     return result
# print(isEven(22))
#
#
# def isOdd(num):
#     # this function checks if a numer is odd
#     result = num % 2 != 0
#     return result
# print(isOdd(10))
#
# # Task2:
# # Create a single function getParity that does the same thing as the two functions in the previous task.
# # This new function will accept a new positional argument of type String
# # that will contain the type of parity we want to get (either odd or even).
#
# def getParity(num, my_string):
#     if my_string == "Odd" or my_string == "odd":
#         return bool(num % 2 != 0)
#     elif my_string == "Even" or my_string == "even":
#         return bool(num % 2 == 0)
#     else:
#         return "Parity indicated is unknown"
#
# print(getParity(1,"Odd"), getParity(2, "even"))
#
# # Task3:
# # Create a single function greet that greets a person differently depending on the time of the day.
#
# import datetime
# my_kw = {"n1": "John", "n2": "Sapir", "d": datetime.datetime.now()}
#
# def greet(**kwargs):
#     name = kwargs["n1"]
#     date = kwargs["d"]
#     if date.hour < 12:
#         return f"Good morning, {name}!"
#     elif 12 <= date.hour <= 18:
#         return f"Good afternoon, {name}!"
#     else:
#         return f"Good night, {name}!"
#
# print(greet(**my_kw))
#
# # Task4:
# # Create a function sumAll that gets the sum of all values in different lists.
# # The function will accept any number of lists, each containing a variable amount of integers.
#
# test1 = [[0, 2, 4, 5]]
# test2 = [[0, 2, 4, 5], [6], [0, 2, 4, 5, 1, 4, 3, 2]]
#
# def sumAll(*lists):
#     # this functions sums a list of items
#     my_sum = 0
#     for i in lists:
#         my_sum += sum(i)
#     return my_sum
#
# print(sumAll(*test2))

# Task5:
#Create a pig_latin function. This function will receive any amount of String objects.
# For each word in those strings, it should transform the word according to these rules:
#If the word starts with vowel, add ay at the end.
#If not, move the first letter to the end and add ay


def pig_latin(*text, suffix="ay", single=False):
    # if the word starts with aeiou it should add ay if not
    # it should move the first letter to the end of the word and add ay

    result = []
    for i in text:
        words = i.split(" ")
        for word in words:
            first_letter = word[0].lower()
            vow = "aeiou"
            if first_letter in vow:
                result.append(word + suffix)
            else:
                result.append((word[1:] + first_letter + suffix).capitalize())
    if single is True:
        return " ".join(result)
    return result         # no need for else here

# test cases:
test1_data = ["Word", "Apple"]
test1_config = {}
print(pig_latin(*test1_data))

test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}
print(pig_latin(*test2_data, **test2_config))

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}
print(pig_latin(*test3_data, **test3_config))