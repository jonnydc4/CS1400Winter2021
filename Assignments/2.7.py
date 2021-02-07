'''
Write a program that calculates and prints the number of minutes in a year.

Assume the following:

1 year = 365 days (Ignore leap years)
1 day = 24 hours
1 hour = 60 minutes
Below is an example of the correct output format:

The number of minutes in a year is X
'''

minute = 1
hour = minute * 60
day = hour * 24
year = day * 365

print(f'The number of minutes in a year is {year}')

