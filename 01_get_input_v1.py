""" Component 1 - Get product details from user
Created by Sammy Cummins
Version 1
29/07/2021
"""

another_product = ""
convert_to_grams = False
convert_to_litres = False
convert_to_kg = False
convert_to_ml = False


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
ml = ["milliliter", "millilitre", "cc", "mL",
      "milliliters", "millilitres", "mls"]
litre = ["liter", "litre", "L", "liters", "litres"]
grams = ["g", "gram", "gms", "grams", "gm"]
kilograms = ["kg", "kilogram", "kilograms"]
all_units = [grams, kilograms, litre, ml]


# String checking function
def str_check(question, error):
    global convert_to_grams
    global convert_to_litres
    global convert_to_ml
    global convert_to_kg
    convert_to_grams = False
    convert_to_litres = False
    convert_to_kg = False
    convert_to_ml = False
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
                    convert_to_kg = True
                elif response in grams:
                    convert_to_grams = True
                elif response in litre:
                    convert_to_litres = True
                elif response in ml:
                    convert_to_ml = True
                return response
            else:
                print(error)

        except ValueError:
            print(error)


product_details = []
all_product_details = []

# Main Routine
money = float(input("How much money would you like to spend? $"))
while money < 10:
    money = float(input("!!You must have at least $10!!\nPlease "
                        "enter how much money you would like to spend: $"))

while another_product.upper() != "YES":
    product_details = []
    another_product = ""
    product_details.append(input("Enter the product name: "))
    product_details.append(str_check("Enter the unit of measurement: ",
                                     "!!Enter a valid measurement (you cannot "
                                     "compare mass to volume)!!"))

    if convert_to_grams:
        product_details.append(num_check("Enter the product mass/volume: ",
                                         "!!Please enter a number "
                                         "above 0!!"))
        if litre in all_units:
            all_units.remove(litre)
            all_units.remove(ml)

    elif convert_to_kg:
        product_details.append(num_check("Enter the product mass/volume: ",
                                         "!!Please enter a number "
                                         "above 0!!")*1000)
        if litre in all_units:
            all_units.remove(litre)
            all_units.remove(ml)

    elif convert_to_litres:
        product_details.append(num_check("Enter the product mass/volume: ",
                                         "!!Please enter a number "
                                         "above 0!!")*1000)
        if grams in all_units:
            all_units.remove(grams)
            all_units.remove(kilograms)

    elif convert_to_ml:
        product_details.append(num_check("Enter the product mass/volume: ",
                                         "!!Please enter a number "
                                         "above 0!!"))
        if grams in all_units:
            all_units.remove(grams)
            all_units.remove(kilograms)

    product_details.append(num_check("Enter the product price: $",
                                     "!!Please enter a price above $0!!"))

    all_product_details.append(product_details)

    another_product = input("Would you like to compare the products yet? ")
    while another_product.upper() != "NO" and another_product.upper() != "YES":
        another_product = input("!!Enter either 'Yes' or 'No'!!\n"
                                "Would you like to compare the products yet? ")

print(all_product_details)
