import random

def standard_dice(dice_max):
    dice_sides = []
    for i in range(dice_max):
        dice_sides.append(i+1)
    return dice_sides

def die_roll(dice_sides):
    dice_side_num = random.randint(0, len(dice_sides) -1)
    return dice_sides[dice_side_num]

def dice_roll(custom, amount, dice):
    dice_sides = []
    if custom:
        dice_sides = dice
    else:
        dice_sides = standard_dice(dice)

    dice_results = []
    for _ in range(amount):
        dice_results.append(die_roll(dice_sides))
    
    return dice_results   
