"""
Exercise 3 - Biography
Author: Ethan Grajo

Date completed: September 16 2024
"""

#i made these inputs detached from the dictionary
#in order to be able to alter it before it gets put into the dictionary

input_name = input("What's your name?: ")
input_hometown = input("Where is your hometown?: ")

#checks for age, if age is not a valid integer, will ask for input again until
#the user gives a valid integer

while True:
    try:
        input_age = int(input("How old are you?: "))
        break
    except ValueError:
        print("Invalid age! You must input an integer. Try again.")

#the dictionary takes in the user input from the first lines and stores it in each appropriate key

information = {
    "name": input_name,
    "age": input_age,
    "hometown": input_hometown,
}

# the dash is used for formatting, just to make the text look a little cleaner

dash = '-' * 50
print(dash)
print("Here is your given information:")

#i ran a for loop to make the code cleaner, the for loop runs through each key-value pair and prints it
#with the print line below.

for k, v in information.items():
    print(f"Your {k} is: {v}")
print(dash)