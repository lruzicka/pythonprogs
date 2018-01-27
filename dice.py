#!/usr/bin/env python3

import sys
import itertools

def generate_dices(sides,total):
    """Generate all dices with the same sides and the same sum of points."""
    values = range(1,total+1)
    possible = []
    combinations = itertools.combinations_with_replacement(values,sides)
    for dice in combinations:
        if sum(dice) == total:
            possible.append(dice)
    return(possible)

def compare_dices(dice0, dice1):
    """Compare two dices and decide the winning one."""
    d0 = 0
    d1 = 0
    for side0 in dice0:
        for side1 in dice1:
            if side1 > side0:
                d1 += 1
            elif side1 < side0:
                d0 += 1
            else:
                pass
    if d1 > d0:
        result = 1
    else:
        result = 0
    return(result)
                
def evaluate(dice0, dices):
    """Compare all dices with the original one and get a list of the winning ones."""
    winning = []
    for dice1 in dices:
        if compare_dices(dice0, dice1) == 1:
            winning.append(dice1)
    try:
        return(winning[0])
    except IndexError:
        return('')
                   
def take_dice(strdice):
    dice = []
    for i in strdice.split(","):
        dice.append(int(i))
    return(dice)
        

try:
    dice0 = take_dice(sys.argv[1])
except IndexError:
    print("No dice given!")
    dice0 = take_dice(input("Dice to compare: "))

dices = generate_dices(len(dice0), sum(dice0))
result = []
for i in evaluate(dice0, dices):
    result.append(str(i))
result = ",".join(result)
print(result)

