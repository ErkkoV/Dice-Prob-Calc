import csv
import os
import ast

def create_rolls_csv_if_not_exists():
    if not os.path.isfile('rolls.csv'):
        with open('rolls.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['result', 'dice_results'])  # Write the header row

def save_rolls(rolls):
    create_rolls_csv_if_not_exists()
    with open('rolls.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['result', 'dice_results'])  # Write the header row
        for roll in rolls:
            writer.writerow([roll['result'], roll['dice_results']])
    

def load_rolls():
    create_rolls_csv_if_not_exists()
    rolls = []
    with open('rolls.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader) 
        for row in reader:
            result = int(row[0])
            dice_results = ast.literal_eval(row[1])
            rolls.append({'result': result, 'dice_results': dice_results})
    return rolls