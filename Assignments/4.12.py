'''
The Payroll Department keeps a list of employee information for each pay period in a text file. The format of each
line of the file is the following: <last name> <hours worked> <hourly wage>

Write a program that inputs a filename from the user and prints to the terminal a report of the wages paid to the
employees for the given period.

The report should be in tabular format with the appropriate header.
Each line should contain:
An employee’s name
The hours worked
The wages paid for that period.
An example of the program input and output is shown below:

Enter the file name: data.txt

Name            Hours      Total Pay
Lambert            34         357.00
Osborne            22         137.50
Giacometti          5         503.50
'''

file_name = input("Enter the file name: ")
file = open(file_name, 'r')
# file_name = "4.12data.txt"

file = open(file_name)
file_contents = file.read()
lines = file_contents.split("\n")

header = ["Name", "Hours", "Total Pay"]
print("\t\t".join(header))

for line_number in range(len(lines)):
    line_variables = lines[line_number].split(" ")
    totalPay = float(line_variables[1]) * float(line_variables[2])
    printArray = [
        line_variables[0],
        line_variables[1],
        str(totalPay)
    ]
    print("\t\t".join(printArray))