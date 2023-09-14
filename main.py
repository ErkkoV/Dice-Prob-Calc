from dice_roller import dice_roller
from roll_input_parser import roll_input_parser

def roll_from_input(roll_input):
    roll = roll_input_parser(roll_input)
    results = dice_roller(*roll)
    print(results)

def guided_roll():
    print('placeholder')

def start_instructions():
    print(
    '''
    Welcome to the dice roller!
    
    You can make guided dice-roll by typing "guided" or pressing any key.
    Or you can manually enter roll directly in a format: "r_dice_amount_d[...dice_sides][rules]:"
    For example: r4d[1,2,2,2,2,3][add1,hgh2] or r5d10[add1,hgh3].
    For more instructions, type "info".
    '''
    )

def info_instructions():
    print('placeholder')

round = 0

while True:
    if (round < 1):
        start_instructions()
    
    user_input = input("\nEnter a roll or command: ")

    if (user_input == "info"):
        info_instructions()
    elif (user_input.startswith('r')):
        roll_from_input(user_input[1:])
    elif (user_input == "" or user_input == "guided"):
        guided_roll()
    else:
        print('Invalid command: type "info" for instruction.')

    round += 1


#example 4d[1,2,2,2,2,3][add1,hgh2]
#example 5d10[add1,hgh3]