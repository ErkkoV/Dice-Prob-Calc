rule_list = {
    "add": "True value, ie: <1>",
    "hgh": "Number of the highest results in the roll added together",
    "lwt": "Number of the lowest results in the roll added together",
}


def rule_adder():
    print("Rules:")
    for index, (key, value) in enumerate(rule_list.items()):
        print(f"Number: {index}, Name: {key}, Value ranges: {value}")

    print("\n")
    print('Press Enter or type "exit" to cancel, or')
    chosen_rule = input(
        "Choose a rule from rules list by typing a number and value, ie: <1, 1> "
    )
    if chosen_rule == "" or chosen_rule == "exit":
        return False
    else:
        keys = list(rule_list.keys())
        return {keys[int(chosen_rule.split(",")[0])]: int(chosen_rule.split(",")[1])}


def guided_roll():
    print("\n")
    dice_amount_input = input(
        "How many dice will you roll, type a number or press enter for 1: "
    )
    if dice_amount_input == "":
        dice_amount_input = 1
    else:
        dice_amount_input = int(dice_amount_input)

    print("\n")
    dice_type_input = input(
        "Will you roll normal die, ie. dice with sides from 1 to n (y), or a die with custom sides (n)"
    )

    print("\n")
    if dice_type_input == "n":
        die_list = input(
            "Enter dice sides as a number list separated by comma, ie: <1, 2, 3, 4, 5, 6> for the normal six sided die: "
        )
        separated_list = die_list.split(",")
        die_sides = [int(side.strip()) for side in separated_list]
        custom_die = True
    else:
        die_max = input(
            "Enter maximun side of the die, ie: 6 for six sided normal die: "
        )
        if die_max == "":
            die_sides = 6
        else:
            die_sides = int(die_max)
        custom_die = False

    print("\n")
    rules = {}
    while True:
        rule = rule_adder()
        if not rule:
            break
        rules.update(rule)

    if rules == {}:
        rules = {"add": True}

    print("\n")
    print(
        f"You roll {dice_amount_input} dices with {die_sides} sides. You use rules: {rules}"
    )

    print("\n")
    return (custom_die, dice_amount_input, die_sides, rules)
