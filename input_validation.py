"""
Module responsible for validating user input
"""

def validate_string(message):

    valid = True
    result = ""

    while valid:

        value = input(message)

        if value.replace(" ", "").isalpha():
            result = value
            valid = False
        else:
            print("Invalid input. Only text values are allowed.")

    return result


def validate_float(message):

    valid = True
    result = 0.0

    while valid:

        value = input(message)

        try:
            result = float(value)
            valid = False
        except ValueError:
            print("Invalid input. Please enter a decimal number.")

    return result


def validate_integer(message):

    valid = True
    result = 0

    while valid:

        value = input(message)

        try:
            result = int(value)
            valid = False
        except ValueError:
            print("Invalid input. Please enter an integer number.")

    return result