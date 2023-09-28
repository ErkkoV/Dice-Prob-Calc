from dice_roller import dice_roller
from roll_input_parser import roll_input_parser
from guided_roll import guided_roll
from instructions import (start_instructions, info_instructions)


def roll_from_input(roll_input):
    roll = roll_input_parser(roll_input)
    results = dice_roller(*roll)
    print(results)

round = 0

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
            guided_roll()
        except:
            print('Invalid guided roll syntax')
    else:
        print('Invalid command: type "info" for instruction.')

    round += 1


#example 4d[1,2,2,2,2,3][add1,hgh2][add1,hgh2]
#example 5d10[add1,hgh3]