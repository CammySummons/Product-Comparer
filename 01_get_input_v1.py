""" Component 1 - Get product details from user
Created by Sammy Cummins
Version 1
29/07/2021
"""

another_product = ""
convert_to_grams = False


# Number checking function
def num_check(question, error):
    valid = False
    while not valid:
        try:
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# Abbreviation lists
# teaspoon = ["tsp", "teaspoon", "t", "teaspoons"]
# tablespoon = ["tbs", "tbsp", "tablespoon", "T", "Tbsp", "tablespoons"]
# ounce = ["oz", "fluid ounce", "fl oz", "ounce", "ounces", "oz."]
# # cup = ["c", "cup", "cups"]
# # pint = ["p", "pt", "fl pt", "pint", "pints", "pt."]
# # quart = ["q", "qt", "fl", "qt.", "quart", "quarts"]
# ml = ["milliliter", "millilitre", "cc", "mL",
#       "milliliters", "millilitres", "mls"]
# litre = ["liter", "litre", "L", "liters", "litres"]
# decilitre = ["deciliter", "decilitre", "dL", "deciliters", "decilitres"]
# pound = ["lb", "lbs", "#", "pound", "pounds", "lb.", "lbs."]
grams = ["g", "gram", "gms", "grams", "gm"]
kilograms = ["kg", "kilogram", "kilograms"]
all_units = [grams, kilograms]


# String checking function
def str_check(question, error):
    global convert_to_grams
    convert_to_grams = False
    in_list = False
    valid = False
    while not valid:
        try:
            response = str(input(question))
            for unit_list in all_units:
                if response in unit_list:
                    in_list = True
            if in_list:
                if response in kilograms:
                    convert_to_grams = True
                return response
            else:
                print(error)

        except ValueError:
            print(error)


product_name = []
product_unit = []
product_mass_volume = []
product_price = []
product_details = [[product_name], [product_unit], [product_mass_volume],
                   [product_price]]


# Main Routine
money = float(input("How much money would you like to spend? $"))
while money < 10:
    money = float(input("!!You must have at least $10!!\nPlease "
                        "enter how much money you would like to spend: $"))

while another_product.upper() != "YES":
    another_product = ""
    product_name.append(input("Enter the product name: "))
    product_unit.append(str_check("Enter the unit of measurement: ", "Error"))

    if convert_to_grams:
        product_mass_volume.append(num_check("Enter the product mass/volume: ",
                                             "!!Please enter a number "
                                             "above 0!!")*1000)
    else:
        product_mass_volume.append(num_check("Enter the product mass/volume: ",
                                             "!!Please enter a number "
                                             "above 0!!"))

    product_price.append(num_check("Enter the product price: $",
                                   "!!Please enter a price above $0!!"))

    another_product = input("Would you like to compare the products yet? ")
    while another_product.upper() != "NO" and another_product.upper() != "YES":
        another_product = input("!!Enter either 'Yes' or 'No'!!\n"
                                "Would you like to compare the products yet? ")

print(product_details)
