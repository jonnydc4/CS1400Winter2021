'''
Project Name: P1 Yondu Udonta
Author: Jonathon Carr
Due Date: MM/DD/YYYY
Course: CS1400-005
My program will ask for 2 inputs; the number of reavers and the amount of units/plunder.
With this info I will be able to divide up the plunder after giving 3 units to each reaver
for celebration purposes. When I divide the plunder I will give a 13% founders fee to the
captain yondu and with what remains a 11% fee to peter. After the founder fees I will divide
the plunder equally between all the reavers. Each share will be rounded down to a
whole number and the extra will be given to the Reaver Benevolent Fund(RBF).
'''

import math
import sys

def main():
    '''
    Program starts here.
    '''

    try:
        reavers = int(input("Enter the number of reavers: "))
        if reavers < 0:
            raise ValueError("Enter positive integers for reavers and units.")
        if reavers < 3:
            raise ValueError("Not enough crew.")

        units = int(input("Enter the number of units: "))
        if units < 0:
            raise ValueError("Enter positive integers for reavers and units.")
        if units < 3:
            raise ValueError("Not enough units.")

    except ValueError as err:
        print(err)
        sys.exit()

    units = units - (3 * (reavers - 2))
    captain_bonus = math.floor(units * .13)
    firstmate_bonus = math.floor((units - captain_bonus) * .11)
    crew_share = math.floor((units - captain_bonus - firstmate_bonus)/ reavers)
    yondu_share = captain_bonus + crew_share
    peter_share = firstmate_bonus + crew_share
    rbf = (units - captain_bonus - firstmate_bonus) - (crew_share * reavers)

    print(f"Yondu's share: {yondu_share}")
    print(f"Peter's share: {peter_share}")
    print(f"Crew: {crew_share}")
    print(f"RBF: {rbf}")



if __name__ == "__main__":
    main()
