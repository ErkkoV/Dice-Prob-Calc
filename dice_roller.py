import random


def standard_dice(dice_max):
    dice_sides = []
    for i in range(dice_max):
        dice_sides.append(i + 1)
    return dice_sides


def die_roll(dice_sides):
    dice_side_num = random.randint(0, len(dice_sides) - 1)
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


def add_dice(dice_results):
    return sum(dice_results)


def dice_sum(dice_results, rules):
    final_result = {}
    if "add" in rules:
        if "hgh" in rules:
            sorted_results = sorted(dice_results, reverse=True)
            calc_results = sorted_results[: rules["hgh"]]
        elif "lwt" in rules:
            sorted_results = sorted(dice_results, reverse=False)
            calc_results = sorted_results[: rules["lwt"]]
        else:
            sorted_results = sorted(dice_results, reverse=True)
            calc_results = sorted_results

        final_result = {
            "result": add_dice(calc_results),
            "dice_results": sorted_results,
        }

    return final_result


# custom, boolean, true if dice has custom values as sides
# amount, integer, amount of dice rolled
# dice, integer or list. Highest side as integer if custom = false, list of integers if true
# dictionary with key-value pairs.
# returns dictionary: {result: integer(total dice sum), dice_results: list[integer](dice rolls)}
def dice_roller(custom, amount, dice, rules):
    return dice_sum(dice_roll(custom, amount, dice), rules)


# print(dice_roller(False, 4, 10, {'add': True, 'hgh': 4}))
