def start_instructions():
    print(
        """
    Welcome to the dice roller!

    Type any command to start!

    Commands:
    "guided:" starts guided roll sequence, also starts guided roll with input "".
    'load': loads currently saved rolls, and shows them. autoload at the start is on by the default
    'save': saves current roll history, autosave is on by the default.
    'info' for more info.
    
    Make a direct roll by typing roll-syntax:
    "r_dice_amount_d[...dice_sides][rules]"
    Examples:
    r4d[1,2,2,2,2,3][add1,hgh2] rolls 4 dices with sides [1, 2, 2, 2, 2, 3], adds two highest results together
    r5d10[add1,hgh3] rolls 5 ten-sided dice, adds 3 highest results together.
    """
    )


def info_instructions():
    print("placeholder")
