'''
An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours, plus any overtime pay.

Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage.

Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours and displays an employee’s total weekly pay.

Below is an example of the program inputs and output:

Enter the wage: $15.50
Enter the regular hours: 40
Enter the overtime hours: 12

The total weekly pay is $899.0
'''

wage = float(input("Enter the wage: "))
reg_hours = int(input("Enter the regular hours: "))
ovrtme_hours = (int(input("Enter the overtime hours: "))) * 1.5

weekly_pay = (wage * reg_hours) + (wage * ovrtme_hours)
print(f'The total weekly pay is {weekly_pay}')