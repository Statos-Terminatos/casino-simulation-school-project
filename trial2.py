from random import *


# This program allows the user to display the percentage of times a given total
# for two dice being rolled. This can be compared with the expected percentage
# for each dice total.

# Generates a random number from 1 to 6 simulating rolling a die
def rollDice():
    return randrange(1, 7)


# Creates a table and display the number of rolls, the percentage of rolls, and
# the expected percentage of rolls for each roll total
def displayResult(rollCount, numTimes):
    actualPercent = [0, 0, 100.0 / 36, 100.0 / 18, 100.0 / 12, 100.0 / 9, 500.0 / 36, 100.0 / 6,
                     500.0 / 36, 100.0 / 9, 100.0 / 12, 100.0 / 18, 100.0 / 36]
    print('Dice Total  Number Occurances  Percentage  Expected Percent')
    for i in range(2, 13):
        print('%5d%12d%22.1f%12.1f' % (i, rollCount[i], float(rollCount[i]) * 100 / numTimes, actualPercent[i]))


# Main Program
print('Simulates rolling two dice')
numTimes = int(input('Enter number of dice rolls: '))
rollCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # initialize list to 0's, 0 and 1 positions actually not used.
for i in range(numTimes):
    die1 = rollDice()
    die2 = rollDice()
    rollCount[die1 + die2] += 1
displayResult(rollCount, numTimes)

