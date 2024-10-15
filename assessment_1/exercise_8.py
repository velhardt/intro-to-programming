"""
Exercise 8 - Simple Search
Author: Ethan Grajo

Date completed: September 18 2024
"""

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] # the base list of names

"""
in this project, i tried 2 different methods to make a scanning program,
one with a while loop, and one with a for loop,
both of these functions make use of the same variables, and
samme methods of checking the names
"""
def search(list, query): #similar to the second function, i make use of two parameters, the given list to search in, and the query to look for,
    i = 0
    while i < len(list):
        if list[i] == query:
            return "Name found in registry"
        i = i + 1
    
    return "Name not found in registry"

def search2(list, query):
    for name in list:
        if name == query:
            return "Name found in registry"
    return "Name not found in registry"

user_input = input("Confirm name in registry: ")
print(search2(names,user_input))
