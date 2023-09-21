from dice_roller import dice_roller
from roll_input_parser import roll_input_parser

rule_list = {
    'add': 'True value, ie: <1>',
    'hgh': 'Number of the highest results in the roll added together',
    'lwt': 'Number of the lowest results in the roll added together',
}

def rule_adder():
    for index, (key, value) in enumerate(rule_list.items()):
        print(f"Number: {index}, Name: {key}, Value ranges: {value}")
    
    print('Press Enter or type "exit" to cancel, or\n')
    chosen_rule = input('Choose a rule from rules list by typing a number and value, ie: <1, 1> ')
    if chosen_rule == '' or chosen_rule == 'exit':
        return False
    else:
        keys = list(rule_list.keys())
        return({keys[int(chosen_rule.split(',')[0])]: int(chosen_rule.split(',')[1])})

def roll_from_input(roll_input):
    roll = roll_input_parser(roll_input)
    results = dice_roller(*roll)
    print(results)

def guided_roll():
    print('\n')
    dice_amount_input = input('How many dice will you roll, type a number or press enter for 1: ')
    if dice_amount_input == '':
        dice_amount_input = 1
    else:
        dice_amount_input = int(dice_amount_input)
    
    print('\n')
    dice_type_input = input('Will you roll normal die, ie. dice with sides from 1 to n (y), or a die with custom sides (n)')
    
    print('\n')
    if dice_type_input == 'n':
        die_list = input('Enter dice sides as a number list separated by comma, ie: <1, 2, 3, 4, 5, 6> for the normal six sided die: ')
        separated_list = die_list.split(',')
        die_sides = [int(side.strip()) for side in separated_list]
        custom_die = True
    else:
        die_sides = int(input('Enter maximun side of the die, ie: 6 for six sided normal die: '))
        custom_die = False

    print('\n')
    rules = {}
    while True:
        rule = rule_adder()
        if not rule:
            break
        rules.update(rule)
        
    print('\n')
    print(f'You roll {dice_amount_input} number of dices with {die_sides} sides. You use rules {rules}')
    
    print('\n')
    result = dice_roller(custom_die, dice_amount_input, die_sides, rules)
    print(result)

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


#example 4d[1,2,2,2,2,3][add1,hgh2][add1,hgh2]
#example 5d10[add1,hgh3]