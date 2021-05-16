"""
Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate
whether or not the triangle is a right triangle.

Recall from the Pythagorean theorem that in a right triangle, the square of one side equals the sum of the squares of
the other two sides.

Use The triangle is a right triangle. and The triangle is not a right triangle. as your final outputs.
An example of the program input and proper output format is shown below:

Enter the first side: 3
Enter the second side: 4
Enter the third side: 5

"""

side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

if side1 > side2 and side1 > side3:

    if side1**2 == side2**2 + side3**2:
        print("The triangle is a right triangle.")

    else:
        print("The triangle is not a right triangle.")

if side2 > side1 and side2 > side3:

    if side2 ** 2 == side1 ** 2 + side3 ** 2:
        print("The triangle is a right triangle.")

    else:
        print("The triangle is not a right triangle.")

if side3 > side1 and side3 > side2:

    if side3 ** 2 == side1 ** 2 + side2 ** 2:
        print("The triangle is a right triangle.")

    else:
        print("The triangle is not a right triangle.")

