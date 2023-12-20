def start_instructions():
    """Prints welcome message and instructions for using the dice roller."""

    print(
        """
    Welcome to the dice roller!

    Type any command to start!

    Commands:
    "guided:" starts guided roll sequence, also starts guided roll with input "".
    'load': loads currently saved rolls, and shows them. autoload at the start is on by the default
    'save': saves current roll history, autosave is on by the default.
    'info' for roll-syntax explation
    
    Make a direct roll by typing roll-syntax:
    "r_dice_amount_d[...dice_sides][rules]"
    Examples:
    r4d[1,2,2,2,2,3][add1,hgh2] rolls 4 dices with sides [1, 2, 2, 2, 2, 3], adds two highest results together
    r5d10[add1,hgh3] rolls 5 ten-sided dice, adds 3 highest results together.
    """
    )


def info_instructions():
    """Prints instructions explaining the roll-syntax for the dice roller."""

    print(
        """
    roll-syntax explained:
    
    r4d[1,2,2,2,2,3][add1,hgh2]
    r5d10[add1,hgh3]

    r   always starts the roll
    4   is amount of dice rolled, can be any integer that is higher than 0
    
    10  is maximum side of the die. In this case die has sides from 1 to 10.
        or
    []  contains a list of custom die sides.
    
    []  contains list of rules, rules are always in format:
            
          add    three letter rule
          1      truth value of the rule, or integer if rule needs it.
          ,      separates rules    
          
          """
    )
