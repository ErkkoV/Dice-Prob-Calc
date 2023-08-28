import math

def standard_dice(dice_max):
    dice_sides = []
    for i in range(dice_max):
        dice_sides.append(i)
    return dice_sides

def die_roll(dice_sides):
    dice_side_num = math.random(1, len(dice_sides))
    return dice_sides[dice_side_num]

def dice_roll(amount, dice):
    dice_sides = []
    if len(dice) > 1:
        dice_results = dice
    elif len(dice) == 1:
        dice_results = standard_dice(dice[0])

    dice_results = []
    for i in range(amount):
        dice_results.append(die_roll(dice_sides))
    
    return dice_results
    
