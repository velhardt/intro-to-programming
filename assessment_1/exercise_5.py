"""
Exercise 5 - Days of the Month
Author: Ethan Grajo

Date completed: September 16 2024
"""

"""
i begin with creating a dictionary, at first, i created simple key-value pairs like 1: 31, but i wanted to integrate
a list in my script that would narrate the month as well, so i made it such that the value is a list, in which both
the month and the number of days can be called.
"""

months = {
    "1" : [31, "January"],
    "2" : [28, "February"],
    "3" : [31, "March"],
    "4" : [30, "April"],
    "5" : [31, "May"],
    "6" : [30, "June"],
    "7" : [31, "July"],
    "8" : [31, "August"],
    "9" : [30, "September"],
    "10" : [31, "October"],
    "11" : [30, "November"],
    "12" : [31, "December"],
}


"""
these lines of print and for loop narrate the numbers
1-12 and their corresponding months, enhancing the programs
clarity and readability
"""

print("-" * 50)
for m_number, data_list in months.items():
    corr_month = months[m_number][1]
    print(f"{m_number} - {corr_month}")
print("-" * 50)


"""
this is the block of code which asks for the users selected month
in order to carry out the task of telling the days of the month.

i put this into a while loop so that in the case of an invalid input;
example = a number not in between 1-12 or a non-integer, it will keep asking
the user to input a value until it is correct

i make use of try-except in tandem with an int(input()) function to catch non-integers
as well as an if condition to check if the number is not within the range of 1-12
"""

while True:
    try:
        query = int(input("Input a month number to know how many days there are in that month: "))
        if query >= 13 or query <= 0:
            print("Invalid month number. try again.")
        else:
            break
    except ValueError:
        print("Invalid input. try again.")


# the reason why i added 'str' before the variable is because i called the user input as an integer
# and the variable can only be called with a string
days = months[str(query)][0] # this calls the amount of days within the given month
month = months[str(query)][1] # this calls the name of the month that the user selected

"""
to account for the month for the leap year; february, i made an if-statement right before the result is narrated
to add 1 day to the [days] value (the base value i set on february is 28, during leap years, there are 29 days, which explains the +1.)
"""
if query == 2:
    while True: #this is within  a while loop so it continuously asks for proper user input
        is_leap = input("Is this February within a leap year? (y/n): ")
        is_leap = is_leap.lower()
        if is_leap == "y":
            days = days + 1
            break
        elif is_leap == "n":
            break
        else:
            print("Invalid input, try again.")

"""
this is the block of code which finally narrates the amount of days in the month
i also added dashes in order to format it nicely, and make it more appealing to look at.
"""
print("-" * 50)
print(f"The amount of days in {month} is {days}!")
print("-" * 50)
