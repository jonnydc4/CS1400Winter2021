'''
In convert.py, define a function decimalToRep that returns the representation of an integer in a given base.

The two arguments should be the integer and the base.
The function should return a string.
It should use a lookup table that associates integers with digits.
A main function that tests the conversion function with numbers in several bases has been provided.

An example of main and correct output is shown below:

def main():
    """Tests the function."""
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))
10
12
1010
A
'''

def decimalToRep(i, b):
    lookup = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    answer = ""
    while i >= b:
        remainder = i % b
        answer = lookup[remainder] + answer
        i = int(i / b)
    return lookup[i] + answer

    # if i < b:
    #     return lookup[i]
    # else:
    #     quotient = int(i / b)
    #     remainder = i % b
    #     return lookup[quotient] + lookup[remainder]


print(10, 10, decimalToRep(10, 10))
print(10, 8, decimalToRep(10, 8))
print(10, 2, decimalToRep(10, 2))
print(10, 16, decimalToRep(10, 16))
