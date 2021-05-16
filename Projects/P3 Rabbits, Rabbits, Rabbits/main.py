'''
Project Name:P3 Rabbits, Rabbits, Rabbits
Author: Jonathon Carr
Due Date:10/17/2020
Course: CS1400-005

My program calculates how many months it will take for a starting pairs of rabbits to reproduce enough to fill 500
rabbit cages. A pair of rabbits has a pair of children every month. Those children are only able to produce after
becoming adults which will take one month. The population will go up exponentially each month. My program will display
this information in the csv file rabbits.csv.
'''

import csv

def main():
    with open('rabbits.csv', 'w', newline='') as my_file:
        writer = csv.writer(my_file)
        writer.writerow(['# Table of rabbit pairs'])

        # Header
        header = ['Month', 'Adults', 'Babies', 'Total']
        writer.writerow(header)

        # Starting Variables
        adults = 1
        babies = 0
        new_adults = 0
        total = adults
        month = 1
        cages = 500
        line1 = [str(month), str(adults), str(babies), str(total)]
        writer.writerow(line1)

        # Function
        while total <= cages:
            month += 1
            new_adults = babies
            babies = adults
            adults = adults + new_adults
            total = adults + babies
            loop_array = [str(month), str(adults), str(babies), str(total)]
            writer.writerow(loop_array)
        writer.writerow(['# Cages will run out in month 14'])

if __name__ == '__main__':
    main()