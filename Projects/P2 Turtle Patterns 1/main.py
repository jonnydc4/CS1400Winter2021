"""
Project Name: P2 Turtle Patterns 1
Author: Jonathon Carr
Due Date: 02/20/2021
Course: CS1400-005

Using a turtle I will draw a scale using a triangle a rectangle and two circles. The program will ask for the width
and height to use as the screen size measurements.
"""

import turtle
import sys
import time

def draw_retangle():
    turtle.pendown()
    turtle.pencolor("grey")
    turtle.fillcolor("brown")
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(200)


    turtle.end_fill()
    turtle.penup()

def draw_circle(radius):
    turtle.pendown()
    turtle.pencolor("light grey")
    turtle.fillcolor("gold")
    turtle.begin_fill()

    turtle.circle(radius)

    turtle.end_fill()
    turtle.penup()

def draw_triangle():
    turtle.pendown()
    turtle.pencolor("black")
    turtle.fillcolor("dark grey")
    turtle.begin_fill()

    for i in range(3):
        turtle.forward(100)
        turtle.left(120)

    turtle.end_fill()
    turtle.penup()

def main():

    try:
        width = int(input("Enter the width: "))
        if width < 0:
            raise ValueError("Enter positive integer for width.")

        height = int(input("Enter the height: "))
        if height < 0:
            raise ValueError("Enter positive integer for height.")

    except ValueError as err:
        print(err)
        sys.exit()

    turtle.screensize(width, height)
    turtle.speed(10)
    turtle.pensize(5)

    turtle.backward(50)
    draw_triangle()
    turtle.goto(0, 85)
    turtle.right(10)
    draw_retangle()
    turtle.goto(-150, 130)
    draw_circle(30)
    turtle.goto(150, 80)
    draw_circle(45)

    time.sleep(5)

if __name__ == "__main__":
    main()
