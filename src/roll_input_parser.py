import re


def roll_input_parser(input):
    """
    Parse input using a regular expression to extract roll components.

    Parameters:
    - input (str): Input string representing a dice roll.

    Returns:
    tuple: A tuple containing (custom, num, roll, rule_components).
           - custom (bool): True if using custom die sides, False otherwise.
           - num (int): Number of dice to roll.
           - roll (list or int): List of custom die sides or the maximum side of the standard die.
           - rule_components (dict): Dictionary containing rule types and their corresponding values.
    """

    roll_pattern = r"(\d+)d(\[?\d+.*?\]?)\[(.*?)\]"

    match = re.match(roll_pattern, input)
    if match:
        num = int(match.group(1))
        roll_str = match.group(2)
        rules = match.group(3)

        if "[" in roll_str:
            roll_list = re.findall(r"\d+", roll_str)
            roll = [int(roll_val) for roll_val in roll_list]
            custom = True
        else:
            roll = int(roll_str)
            custom = False

        rule_components = {}

        for rule in rules.split(","):
            rule_match = re.match(r"([a-zA-Z]+)(\d+)", rule.strip())
            if rule_match:
                rule_type = rule_match.group(1)
                rule_value = int(rule_match.group(2))
                rule_components[rule_type] = rule_value

        return custom, num, roll, rule_components
    else:
        raise ValueError("Input format not valid")
