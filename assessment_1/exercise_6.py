"""
Exercise 6 - Brute Force Attack
Author: Ethan Grajo

Date completed: September 17 2024
"""


"""
i opted to turn the correct_pw into a string as opposed to an int, because it would be easier to leave it as such instead of 
looking for int inputs, which may result in having to look for int inputs, which will need 
additional lines of code in order to create a fallback.
the fallback being a try-except in order to catch a non-int input, which is redundant when turning the '12345
into string.
"""

correct_pw = "12345" 
attempts = 5
"""
the block of code is under a while loop to ensure that the user can keep repeating, however
in the case of maximum attempts being used, the loop will break, disallowing the user to attempt
any longer.

similarly, if the password is correct, the loop will be broken and the code will stop.
"""
while True:
    guess = input("Please enter password: ")
    if guess == correct_pw:
        print("Welcome back, user.")
        break
    else:
        attempts = attempts - 1 #this reduces the 'attempts' variable by 1, it will then check if it is 0, in which the code stops
        if attempts == 0:
            print("You have run out of attempts, this account has temporarily been shutdown and the authorities have been notified.")
            break

        # i deliberately didnt use an else after the previous if-statement, because if the above statement were to be fulfilled,
        # the loop would be terminated. on the other hand, if it were not fulfilled, the following print would have run regardless

        print(f"Incorrect password. You have {attempts} attempts left.") #i opted to use f-string function in prints to make syntax easier
