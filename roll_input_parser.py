import re

def roll_input_parser(input):
    roll_pattern = r'(\d+)d(\[?\d+.*?\]?)\[(.*?)\]'

    match = re.match(roll_pattern, input)
    if match:
        num = int(match.group(1))
        roll_str = match.group(2)
        rules = match.group(3)

        if '[' in roll_str:
            roll_list = re.findall(r'\d+', roll_str)
            roll = [int(roll_val) for roll_val in roll_list]
        else:
            roll = int(roll_str)

        rule_components = []

        for rule in rules.split(','):
            rule_match = re.match(r'([a-zA-Z]+)(\d+)', rule.strip())
            if rule_match:
                rule_type = rule_match.group(1)
                rule_value = int(rule_match.group(2))
                rule_components.append((rule_type, rule_value))

        return num, roll, rule_components
    else:
        raise ValueError("Input format not valid")
    
# print(roll_input_parser("3d[6,8,10][add2,bes51,mul3]"))

# Example input
# input_str = "3d[6,8,10][add2,bes51,mul3]"

# example use
# num, roll, rule_components = roll_input(input_str)

# print("Number of rolls:", num)
# print("Sides on the dice:", roll)
# print("Rule components:", ", ".join([f"{rule_type}{rule_value}" for rule_type, rule_value in rule_components]))