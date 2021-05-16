'''
Jonathon Carr
CS-1400-007
11/14/2020
Turtle Patterns II

I learned how to make functions to simplify my code more.
I learned how to make size work as a possible input for the scene.
I learned how that I needed to draw a canvas to change the backround color to draw two pictures in one.
'''


import turtle

'''
Draw Canvas determines the size and color of my canvas.
'''

def draw_canvas(size, color):
    # assumes heading and location have been set before calling function
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

'''
Draw branch draws each the triangles that will form the trees.
'''
def draw_branch(branch_width):
    turtle.pendown()
    turtle.fillcolor('green')
    turtle.begin_fill()
    turtle.forward(branch_width)
    turtle.left(120)
    turtle.forward(branch_width)
    turtle.left(120)
    turtle.forward(branch_width)
    turtle.left(120)
    turtle.end_fill()
    turtle.penup()

'''
Move up one branch will put the turtle in position to draw the next branch.
'''

def move_up_one_branch(space_between_branches):
    turtle.left(90)
    turtle.forward(space_between_branches)
    turtle.right(90)

'''
Draw pine combines the two previous functions to draw a full tree.
'''
def draw_pine(trunk_width):
    trunk_height = trunk_width * 4
    branch_width = trunk_width * 5
    space_between_branches = branch_width / 3
    num_branches = 4

    # draw tree trunk
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(trunk_height)
    turtle.right(90)
    turtle.forward(trunk_width)
    turtle.right(90)
    turtle.forward(trunk_height)
    turtle.right(90)
    turtle.forward(trunk_width)
    turtle.right(90)
    turtle.end_fill()

    # move to first branch
    turtle.penup()
    turtle.forward(trunk_height)
    turtle.left(90)
    turtle.forward((branch_width / 2) - (trunk_width / 2))
    turtle.right(180)

    for i in range(num_branches):
        draw_branch(branch_width)
        move_up_one_branch(space_between_branches)

    # move back to ground level
    turtle.right(90)
    turtle.forward(trunk_height + (space_between_branches * num_branches))
    turtle.left(90)

    # move to right of tree
    turtle.forward((branch_width / 2) - (trunk_width / 2))
    turtle.forward(trunk_width)

'''
This function will draw a mountain.
'''

def draw_mountain(size):
    mountain_size = size
    turtle.fillcolor('purple')
    turtle.begin_fill()

    turtle.pendown()
    for i in range(3):
        turtle.forward(mountain_size)
        turtle.left(120)
    turtle.end_fill()

    turtle.penup()
    turtle.right(120)
    turtle.backward(mountain_size)
    turtle.pendown()

    turtle.fillcolor('white')
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(mountain_size/4)
        turtle.left(120)
    turtle.end_fill()
    turtle.penup()
    turtle.left(120)

'''
Draw scene will use all the previous functions to produce the final product image.
'''

def draw_scene(color, size, startX, startY, heading):

    # go to starting location
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.setheading(heading)

    # draw canvas
    draw_canvas(size, color)

    # turn cursor back to the correct heading
    turtle.right(90)
    draw_mountain(size)

    # go to starting location
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.setheading(heading)
    turtle.right(90)

    num_trees = 8
    num_spaces_between_trees = num_trees + 1
    space_tree_ratio = 5
    tree_width = size / (num_trees + (space_tree_ratio * num_spaces_between_trees))
    space_between_trees = space_tree_ratio * tree_width

    for i in range(num_trees):
        turtle.forward(space_between_trees)
        turtle.left(90)
        draw_pine(tree_width)

    return

    # go back to starting position before drawing trees
    turtle.penup()
    # draw trees
    x = startX
    for tree in range(10):
        turtle.penup()
        turtle.forward()
        draw_pine(picture_size)
        x += (picture_size/10)
    else:
        turtle.penup()
        turtle.goto(picture_size/10, picture_size/2)
        draw_cloud(picture_size)

'''
This main function gets a user input for what time of day the scene will be and runs the algorithm
'''

def main():
    time_of_day = input("Enter Daytime, Nightime, Sunrise, or Sunset: ")

    # Set screen color for each time of day
    if time_of_day == "Daytime":
        canvas_color = 'light blue'
    elif time_of_day == "Nightime":
        canvas_color = 'black'
    elif time_of_day == "Sunrise" or time_of_day == "Sunset":
        canvas_color = 'gold'
    else:
        print("Must enter the time of day correctly")
        exit(0)

    # set screen size
    screen = turtle.Screen()
    screen.setup(600, 600)
    turtle.speed(0)

    # draw first scene
    draw_scene(canvas_color, 500, -250, -250, 90)

    # draw 2nd scene
    draw_scene('gold', 200, -75, 75, 45)

    # dont close python until you close the screen
    screen.mainloop()


if __name__ == '__main__':
    main()