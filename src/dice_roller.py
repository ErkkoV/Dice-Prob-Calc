import random


def standard_dice(dice_max):
    return [i + 1 for i in range(dice_max)]


def die_roll(dice_sides):
    return random.choice(dice_sides)


def dice_roll(custom, amount, dice):
    dice_sides = []
    if custom:
        dice_sides = dice
    else:
        dice_sides = standard_dice(dice)

    return [die_roll(dice_sides) for _ in range(amount)]


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


def dice_roller(custom, amount, dice, rules):
    return dice_sum(dice_roll(custom, amount, dice), rules)
