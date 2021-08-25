""" Component 5 - Function to check that no inputs are left blank
Created by Sammy Cummins
Version 1
10/08/2021
"""


# Checks that the input is not blank
def blank_checker(question, error):
    valid = False
    while not valid:
        response = input(question).strip()
        if response == "":
            print(error)
        else:
            return response


# Main Routine
detail = blank_checker("Enter something: ", "You can't leave this blank!")

