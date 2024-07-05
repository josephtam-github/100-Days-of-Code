#!/bin/usr/python3


""" Create a function that takes two lists and returns a new list
containing elements that are in the first list but not in the second.
"""


def list_difference(list1, list2):
    return list(set(list1) - set(list2))


# Test the function
list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [2, 4, 6, 8]
result = list_difference(list_a, list_b)
print(f"Elements in list_a but not in list_b: {result}")


""" Write a function that merges two dictionaries.

If there are duplicate keys,
the value from the second dictionary should be used.
"""


def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}


# Test the function
dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'b': 4, 'd': 5, 'e': 6}
result = merge_dicts(dict_a, dict_b)
print(f"Merged dictionary: {result}")


""" Create a function that takes a string and returns a tuple containing:
The string with all vowels removed
A list of all the removed vowels
"""


def process_vowels(text):
    vowels = 'aeiouAEIOU'
    removed_vowels = []
    result_string = ''

    for char in text:
        if char in vowels:
            removed_vowels.append(char)
        else:
            result_string += char

    return (result_string, removed_vowels)


# Test the function
test_string = "Hello, World! How are you?"
result = process_vowels(test_string)
print(f"String without vowels: {result[0]}")
print(f"Removed vowels: {result[1]}")


""" Write a function that takes two sets and returns a tuple containing:

The intersection of the sets
The symmetric difference of the sets
"""


def set_operations(set1, set2):
    intersection = set1.intersection(set2)
    symmetric_difference = set1.symmetric_difference(set2)
    return (intersection, symmetric_difference)


# Test the function
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}
result = set_operations(set_a, set_b)
print(f"Intersection: {result[0]}")
print(f"Symmetric Difference: {result[1]}")
