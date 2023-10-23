from dice_roller import dice_roller
from roll_input_parser import roll_input_parser
from guided_roll import guided_roll
from instructions import (start_instructions, info_instructions)
from saving import (load_rolls, save_rolls)

roll_history = []

def roll_from_input(roll_input):
    roll = roll_input_parser(roll_input)
    results = dice_roller(*roll)
    print(results)
    roll_history.append(results)

def guided_rolling():
    roll = guided_roll()
    results = dice_roller(*roll)
    print(results)
    roll_history.append(results)

round = 0
saved = False

while True:
    if (round < 1):
        start_instructions()
    
    user_input = input("\nEnter a roll or command: ")

    if (user_input == "info"):
        try:
            info_instructions()
        except:
            print('Invalid instruction syntax')
    elif (user_input.startswith('r')):
        try:
            roll_from_input(user_input[1:])
        except:
            print('Invalid roll syntax')
    elif (user_input == "" or user_input == "guided"):
        try:
            guided_rolling()
        except:
            print('Invalid guided roll syntax')
    elif (user_input == 'load'):
        try:
            rolls = load_rolls()
            print('Loaded rolls:')
            for roll in rolls:
                roll_history.append(roll)
                print(roll)
        except:
            print('Error in loading rolls')
    elif (user_input == 'save'):
        try:
            save_rolls(roll_history)
        except:
            print('Error in saving rolls')

    else:
        print('Invalid command: type "info" for instruction.')

    round += 1


#example 4d[1,2,2,2,2,3][add1,hgh2][add1,hgh2]
#example 5d10[add1,hgh3]