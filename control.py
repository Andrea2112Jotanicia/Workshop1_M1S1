"""
Module responsible for controlling program continuation
"""

def continue_register():

    control = True
    result = True

    while control:

        answer = input("Do you want to register another sale? (y/n): ").lower()

        if answer == "y":
            result = True
            control = False

        elif answer == "n":
            result = False
            control = False

        else:
            print("Invalid option. Please enter y or n.")

    return result