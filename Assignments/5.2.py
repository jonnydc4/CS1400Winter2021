'''
Write a program that allows the user to navigate the lines of text in a file. The program should prompt the user for a
filename and input the lines of text into a list. The program then enters a loop in which it prints the number of lines
in the file and prompts the user for a line number. Actual line numbers range from 1 to the number of lines in the file.
If the input is 0, the program quits. Otherwise, the program prints the line associated with that number.

An example file and the program input and output is shown below:

5.2example.txt

Line 1.
Line 2.
Line 3.

Enter the input file name: 5.2example.txt

The file has 3 lines.
Enter a line number [0 to quit]: 2
2 :  Line 2.
The file has 3 lines.
Enter a line number [0 to quit]: 4
ERROR: line number must be less than 3.
The file has 3 lines.
Enter a line number [0 to quit]: 0
'''

# get file input
filename = input("Enter the input file name: ")

while True:
    # get line input
    line = int(input("Enter a line number [0 to quit]: "))

    # create the array using the file
    f = open(filename, 'r')
    file = f.read()
    array = file.split('\n')

    # count how many lines are in the file
    line_number = 0
    for x in array:
        line_number += 1
        pass

    print(f'The file has {line_number} lines')

    # loop to print the specified input line
    if line > line_number:
        print(f'ERROR: line number must be less than {line_number}')
    else:
        if line != 0:
            print(array[(line - 1)])
        else:
            exit()

    # close the file (very important for this assignment)
    f.close()
