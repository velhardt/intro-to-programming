"""
Exercise 8 - Simple Search
Author: Ethan Grajo

Date completed: September 18 2024
"""

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
def search(list, query):
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