"""
Exercise 7 - Some Counting
Author: Ethan Grajo

Date completed: September 17 2024
"""

# Write a loop that counts up from 0 to 50 in increments of 1.
def loop_1():
    for n in range(51):
        print(n)

# Write a loop that counts down from 50 to 0 in decrements of 1.
def loop_2():
    for n in reversed(range(51)):
        print(n)

# Write a loop that counts up from 30 to 50 in increments of 1.
def loop_3():
    for n in range(30,51):
        print(n)

# Write a loop that counts down from 50 to 10 in decrements of 2.
def loop_4():
    for n in range(50,8,-2):
        print(n)

# Write a loop that counts up from 100 to 200 in increments of 5.
def loop_5():
    for n in range(100,205,5):
        print(n)

"""
i wanted to make all the loops viewable in one script, so i created a map of different
possible inputs and their related functions and descriptions, for further explanation;
the key = the input that the user will provide
the value = a list comprising of 1; the function name to be called and 2; the description
"""

command_key = {
    "1": [loop_1, "A loop that counts up from 0 to 50 in increments of 1."],
    "2": [loop_2, "A loop that counts down from 50 to 0 in decrements of 1."],
    "3": [loop_3, "A loop that counts up from 30 to 50 in increments of 1."],
    "4": [loop_4, "A loop that counts down from 50 to 10 in decrements of 2."],
    "5": [loop_5, "A loop that counts up from 100 to 200 in increments of 5."],
}

"""
this is the loop that will continuously ask the user for the input, which will then display
the loop that corresponds to the number inputted

it will keep looping in case of an invalid input, and will ask the user for a valid
input

i also created an option to list down the available functions/loops within the script,
which can be called by inputting 'list'
"""

while True:
    user_input = input("In this panel, you can view 5 different demonstrations of 'for loops'.\nTo proceed, type 'list' to see the list of possible loops you can access.\nOtherwise, input a number between 1-5.\nInput: ")
    if user_input == "list": # this input will display the available loops
        print("-"*85)
        for k,v in command_key.items(): # this for loop prints out the available numbers and their respective descriptions
            description = command_key[k][1] # since the value in the dictionary is a list, it takes the given value in the respective iteration of the loop
            print(f"[{k}] - {description}")
        print("-"*85)

    elif user_input.isdigit(): # this is to check if the input of the user is a digit, or a number
        if int(user_input) in range(1,5): # check if the input is valid, in this case, we have 5 inputs, so it checks if the input is valid from 1-5
            print("-"*85)
            command_key[user_input][0]() # calls the function and prints out the given loop
            print("-"*85)
            print(f"Displayed loop is: {command_key[user_input][1]}") # this narrates which loop is currently displayed
            break
        else:
            print("-"*85)
            print("Invalid input. Please try again.")
            print("-"*85)
    else:
        print("-"*85)
        print("Invalid input. Please try again.")
        print("-"*85)

"""
i made several else conditions due to the large conditional trees,
but they all serve the same purpose
"""