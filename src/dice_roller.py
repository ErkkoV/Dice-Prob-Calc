import random


def standard_dice(dice_max):
    """
    Generate a list representing standard dice with values from 1 to dice_max.

    Parameters:
    - dice_max (int): The maximum value of the standard dice.

    Returns:
    list: List of integers representing standard dice.
    """
    return [i + 1 for i in range(dice_max)]


def die_roll(dice_sides):
    """
    Simulate the roll of a die with the given sides.

    Parameters:
    - dice_sides (list): List of possible values for the die

    Returns:
    int: The result of the die roll.
    """
    return random.choice(dice_sides)


def dice_roll(custom, amount, dice):
    """
    Roll a specified number of dice with customizable sides.

    Parameters:
    - custom (bool): If True, use the provided dice list; if False, use standard dice.
    - amount (int): The number of dice to roll.
    - dice (list): List of possible values for the dice (if custom is True) or the maximum value of standard dice.

    Returns:
    list: List of results from rolling the dice.
    """
    dice_sides = dice if custom else standard_dice(dice)
    return [die_roll(dice_sides) for _ in range(amount)]


def add_dice(dice_results):
    """
    Calculate the sum of the values in the given list.

    Parameters:
    - dice_results (list): List of values to be summed.

    Returns:
    int: The sum of the values in the list.
    """
    return sum(dice_results)


def dice_sum(dice_results, rules):
    """
    Calculate the sum of dice results based on specified rules.

    Parameters:
    - dice_results (list): List of dice results to be processed.
    - rules (dict): Dictionary containing rules for processing the dice results.
                   Supported rules: "add", "hgh" (highest), "lwt" (lowest).

    Returns:
    dict: Dictionary containing the final result and the sorted dice results based on rules.
    """
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
    """
    Perform a dice roll, process the results based on specified rules, and return the final result.

    Parameters:
    - custom (bool): If True, use the provided dice list; if False, use standard dice.
    - amount (int): The number of dice to roll.
    - dice (list): List of possible values for the dice (if custom is True) or the maximum value of standard dice.
    - rules (dict): Dictionary containing rules for processing the dice results.
                   Supported rules: "add", "hgh" (highest), "lwt" (lowest).

    Returns:
    dict: Dictionary containing the final result and the sorted dice results based on rules.
    """
    return dice_sum(dice_roll(custom, amount, dice), rules)
