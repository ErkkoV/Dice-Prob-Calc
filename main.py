from dice_roller import dice_roller
from roll_input_parser import roll_input_parser

def get_roll_input():
    x = input("Insert dice roll:  ")
    return roll_input_parser(x)

while True:
    roll = get_roll_input()
    results = dice_roller(*roll)
    print(results)

#example 4d[1,2,2,2,2,3][add1,hgh2]
#example 5d10[add1,hgh3]