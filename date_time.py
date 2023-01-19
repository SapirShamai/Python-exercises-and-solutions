# A datetime module can be used to represent a time, we shall use the .now() method to get the current year.
# To see what you can possibly do with the instance of datetime, experiment with the existing methods.
#from datetime import datetime
#
# current_datetime = datetime.now()
# x = dir(current_datetime)
# print(current_datetime)
#

# Task 1
# Using the variable called current_datetime, print out the current year

import datetime
current_datetime = datetime.datetime.now().year
print("Current year : ", current_datetime)

# # Task 2
# # Using the variable called some_date, print out the current week day

some_date = datetime.datetime.now().isoweekday()
print("Current day of the week : ", some_date)

# Task 3
# Write a Python program to determine whether the year 2021 is a leap year.

import calendar

user_year = int(input("Enter year : "))
answer = calendar.isleap(user_year)

if answer == False:
    print(user_year, "is NOT a leap year!")
else:
    print(user_year, "IS a leap year!")

# Task 4:
# Your task is to convert a user provided string into a datetime object.

date_as_string = input("Enter date and time according to this format: 'Feb 14 2021 8:30AM' : ")
#date_as_string = "Feb 14 2021 8:30AM"
new_date = datetime.datetime.strptime(date_as_string, "%b %d %Y %I:%M%p")
print(new_date)