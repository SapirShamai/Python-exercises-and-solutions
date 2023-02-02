# You are given a two dimensional list of numbers.
# Calculate the mean of those numbers by implementing a mean method that takes a list as an argument.

numbers = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]


def mean(numbers):

    new_list = []
    for small_list in numbers:
        new_list.append(round(sum(small_list) / len(small_list)))
    return new_list


print(mean(numbers))