'''
Write and test a program that computes the area of a circle.

Request a number representing a radius as input from the user.
Use the formula 3.14 × radius^2 to compute the area.
Output this result with a suitable label.
An example of the program input and output is shown below:

Enter the radius: 5
The area is 78.5 square units.
'''

radius = float(input("Enter the radius: "))
pi = 3.14
area =  pi * (radius * radius)
print(f'The area is {area} square units.')
