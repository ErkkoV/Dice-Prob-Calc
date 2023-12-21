import csv
import os
import ast

csv_path = os.path.join("src", "rolls.csv")


def create_rolls_csv_if_not_exists():
    """Create rolls.csv with header if it doesn't exist."""
    if not os.path.isfile(csv_path):
        with open(csv_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["result", "dice_results"])  # Write the header row


def save_rolls(rolls):
    """Save rolls to rolls.csv."""
    create_rolls_csv_if_not_exists()
    with open(csv_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["result", "dice_results"])  # Write the header row
        for roll in rolls:
            writer.writerow([roll["result"], roll["dice_results"]])


def load_rolls():
    """Load rolls from rolls.csv."""
    create_rolls_csv_if_not_exists()
    rolls = []
    with open(csv_path, mode="r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            result = int(row[0])
            dice_results = ast.literal_eval(row[1])
            rolls.append({"result": result, "dice_results": dice_results})
    return rolls
