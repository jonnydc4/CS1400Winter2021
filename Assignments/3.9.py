'''
Edit the program provided so that it receives a series of numbers from the user and allows the user to press the enter
key to indicate that he or she is finished providing inputs. After the user presses the enter key,
the program should print:

The sum of the numbers
The average of the numbers

An example of the program input and output is shown below:

Enter a number or press Enter to quit: 1
Enter a number or press Enter to quit: 2
Enter a number or press Enter to quit: 3
Enter a number or press Enter to quit:

The sum is 6.0
The average is 2.0
'''

iteration = 0
theSum = 0.0
data = input("Enter a number: ")
while data != "":
    iteration += 1
    number = float(data)
    theSum += number
    data = input("Enter the next number: ")
print("The sum is", theSum)
print("The average is", theSum/ iteration)
