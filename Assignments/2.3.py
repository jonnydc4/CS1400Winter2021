'''
Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to buy LP record albums.
The store rents new videos for $3.00 a night, and oldies for $2.00 a night.

Write a program that the clerks at Five Star Retro Video can use to calculate the total charge for a customer’s video rentals.

The program should prompt the user for the number of each type of video and output the total cost.

An example of the program input and output is shown below:

Enter the number of new videos: 3
Enter the number of oldies: 2

The total cost is $13.0
'''

new_vids = int(input("Enter the number of new videos: "))
old_vids = int(input("Enter the number of old videos: "))

new_cost = float(new_vids * 3.00)
old_cost = float(old_vids * 2.00)

total_cost = new_cost + old_cost

print(total_cost)