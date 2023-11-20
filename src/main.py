import os
from dice_roller import dice_roller
from roll_input_parser import roll_input_parser
from guided_roll import guided_roll
from instructions import start_instructions, info_instructions
from saving import load_rolls, save_rolls

auto_save = False
auto_load = False

try:
    settings_path = os.path.join("src", "settings.txt")
    with open(settings_path, "r") as file:
        for setting in file:
            if setting.startswith("AUTOSAVE"):
                auto_save = setting.split("=")[1].strip() == "True"

            if setting.startswith("AUTOLOAD"):
                auto_load = setting.split("=")[1].strip() == "True"
except:
    print("Error in loading settings")


def roll_from_input(roll_input):
    roll = roll_input_parser(roll_input)
    results = dice_roller(*roll)
    print(results)
    roll_history.append(results)
    if auto_save:
        save_rolls(roll_history)


def guided_rolling():
    roll = guided_roll()
    results = dice_roller(*roll)
    print(results)
    roll_history.append(results)
    if auto_save:
        save_rolls(roll_history)


round = 0


while True:
    if round < 1:
        if auto_load:
            try:
                roll_history = load_rolls()
                print("Rolls autoloaded")
            except:
                print("Error in loading rolls")

        start_instructions()

    user_input = input("\nEnter a roll or command: ")

    if user_input == "info":
        try:
            info_instructions()
        except:
            print("Invalid instruction syntax")
    elif user_input.startswith("r"):
        try:
            roll_from_input(user_input[1:])
        except:
            print("Invalid roll syntax")
    elif user_input == "" or user_input == "guided":
        try:
            guided_rolling()
        except:
            print("Invalid guided roll syntax")
    elif user_input == "load":
        try:
            rolls = load_rolls()
            print("Loaded rolls:")
            for roll in rolls:
                roll_history.append(roll)
                print(roll)
        except:
            print("Error in loading rolls")
    elif user_input == "save":
        try:
            save_rolls(roll_history)
        except:
            print("Error in saving rolls")

    else:
        print('Invalid command: type "info" for instruction.')

    round += 1
