from turtle import Turtle
from scipy.stats import variation
from numpy import random, mean, max, min
from math import hypot

'''
Jonathon Carr
CS1400-007
12/5/20
P6 Random walks

My program will be able to track the random walks of Pa, Mi-Ma, and Reg. It will return the maximum and minimum
distance of each walk as well as the mean and the coefficient of variance.

Instructions:

When asked to enter steps, you can enter integer numbers only. Multiple can be entered if they are separated by a comma. 
Negative numbers will not work nor anything under 3.

When asked to enter trials, you can only enter one integer value. Negative numbers will not work nor anything under 3.

When asked to enter subject, the options will only be "Pa", "Mi-ma", "Reg", or "all".
'''

# configure turtle
screen = Turtle()
screen.speed(0)

'''
get_one_walk determines which walk will be done and for how many times. It also performs the walks and 
plots the points.
'''
def get_one_walk(subject, numSteps):
    # print(f"{subject} is taking a walk of {numSteps} steps")
    x = 0
    y = 0
    color = ""

    # take all your steps
    if subject == 'Pa':
        color = "blue"
        for stepDirection in random.randint(4, size=(int(numSteps))):
            if stepDirection == 0:
                x = x + 1
            if stepDirection == 1:
                y = y + 1
            if stepDirection == 2:
                x = x - 1
            if stepDirection == 3:
                y = y - 1

    if subject == 'Mi-ma':
        color = "red"
        for stepDirection in random.randint(6, size=(int(numSteps))):
            if stepDirection == 0:
                x = x + 1
            if stepDirection == 1:
                y = y + 1
            if stepDirection == 2:
                x = x - 1
            if stepDirection >= 3:
                y = y - 1

    if subject == 'Reg':
        color = "green"
        for stepDirection in random.randint(2, size=(int(numSteps))):
            if stepDirection == 0:
                x = x + 1
            if stepDirection == 1:
                x = x - 1

    # calculate distance from ending position to 0,0
    walk_distance = hypot(x, y)

    # plot x and y
    screen.penup()
    screen.goto(x, y)
    screen.pendown()
    screen.dot(5, color)



    # return the distance between where you ended up and 0,0
    return walk_distance

'''
get_walks_array makes an array with all of the walk distances. It also prints which walk is being done and 
how many times.
'''

def get_walks_array(subject, numWalks, numSteps):
    print(f"{subject} random walk of {numSteps} steps {numWalks} times")
    walk_array = []
    for trials in range(1, numWalks):
        walk_distance = get_one_walk(subject, numSteps)
        walk_array.append(walk_distance)

    # return an array of distances where you ended up distance to 0,0
    return walk_array

'''
do_many_trials takes the array made from get_many_walks and uses it to get the max, min, mean, and CV of the walks 
performed. It then prints that information.
'''

def get_outputs(subject, walkList, numWalks):
    for numSteps in walkList.split(','):
        all_walks = get_walks_array(subject, numWalks, numSteps)

        # calculate stats
        walks_mean = mean(all_walks)
        walks_max = max(all_walks)
        walks_min = min(all_walks)
        walks_variance = variation(all_walks)

        # print stats
        print(f'Mean = {walks_mean} CV = {walks_variance} \nMax = {walks_max} Min = {walks_min}')

'''
random_walks hold parameters for the command-line inputs
'''

def random_walks(walkList, numWalks, subject):
    # walkList of "10,100" is a comma-delimited list of walks to take and each number is the number of steps
    # numWalks is the number of walks to do in order to calculate max, min, mean, variance
    # subject is “Pa”, “Mi-Ma” or “Reg” or "all"

    walks = walkList.split(",")
    if subject in ["Pa", 'all']:
        get_outputs("Pa", walkList, numWalks)
    if subject in ["Mi-ma", 'all']:
        get_outputs("Mi-ma", walkList, numWalks)
    if subject in ["Reg", 'all']:
        get_outputs("Reg", walkList, numWalks)

    return

'''
The main function takes the command line inputs and runs the program.
'''

def main():
    steps = input("Enter steps: ")
    trials = int(input("Enter trials: "))
    subject = input("Enter Subject: ")
    if trials < 3:
        print("Enter something larger or equal to 3 for trials")
        exit()
    elif int(steps) < 3:
        print("Enter something larger or equal to 3 for steps")
        exit()
    elif subject in ["Pa", "Mi-ma", "Reg", 'all']:
        pass
    else:
        print("Please enter a valid subject")
        exit()
    random_walks(steps, trials, subject)

main()
