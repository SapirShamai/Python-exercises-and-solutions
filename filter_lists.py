# You are given a list of strings. Some of those strings may contain integers, for example Digital Car33r Institute.
# Implement a method digit_filter that takes a list of strings as an argument
# and only returns those strings that don't contain a number.


import re
def digit_filter(list):
    new_list = []
    for item in list:
        match = re.match('.*\d', item)
        if not match:
            new_list.append(item)
    return new_list

l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']
print(digit_filter(l33t))
