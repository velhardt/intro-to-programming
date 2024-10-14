"""
Exercise 10 - Is it even?
Author: Ethan Grajo

Date completed: September 18 2024
"""
def num_check(n):
    if n % 2 == 0:
        return "Given number is even."
    else:
        return "Given number is odd."

def main_func():
    while True:
        try:
            number = int(input("Please enter a number to determine if it is even or odd: "))
            break
        except ValueError:
            print("Invalid input. Please input an integer.")
    print(num_check(number))

if __name__ == "__main__":
    main_func()