# Modify the code below
"""
File: newton.py
Project 6.1

Compute the square root of a number (uses function with loop).

1. The input is a number, or enter/return to halt the
   input process.

2. The outputs are the program's estimate of the square root
   using Newton's method of successive approximations, and
   Python's own estimate using math.sqrt.
"""


import math

# Receive the input number from the user

def newton(x):

    # Initialize the tolerance and estimate
    tolerance = 0.000001
    estimate = 1.0

    # Perform the successive approximations
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break

    # Output the result
    print("The program's estimate is", estimate)
    print("Python's estimate is", math.sqrt(x))

def main():
    while True:
        x = input("Enter a positive number: ")
        if x != "":
            newton(float(x))
        else:
            exit()
main()
