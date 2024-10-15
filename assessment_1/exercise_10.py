"""
Exercise 10 - Is it even?
Author: Ethan Grajo

Date completed: September 18 2024
"""
def num_check(n):
    if n % 2 == 0: # i make use of the modulus formula to check if a number is odd or even
        return "Given number is even." # instead of printing in this checking function, i return a value to be printed later on
    else:
        return "Given number is odd."

def main_func():
    while True: #i make use of a while loop in order to avoid error, making the user re-enter their input  in the case that it is invalid
        try: # the try/except function is helpful in catching a non-integer input, within the loop, if the input was not an integer, it will go to the break function
            number = int(input("Please enter a number to determine if it is even or odd: ")) 
            break # when the input is a valid integer, the loop will break, continuing on to the rest of the code
        except ValueError:
            print("Invalid input. Please input an integer.") # when the input is invalid, it will tell the user, not breaking the loop, which will then ask for the input again
    print(num_check(number)) # finally, when the loop is broken, the result will be printed by executing the function inside a print, which will display if the given integer is odd or even

if __name__ == "__main__":
    main_func()
