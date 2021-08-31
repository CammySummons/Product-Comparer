""" Product Comparer - Full working program with changes made in relation to
feedback given in usability
Created by Sammy Cummins
Version 4
30/08/2021
"""

# List Declaration
price_per_unit_list = []  # Contains the price/mass for each product
price_per_unit = []
prices = []
cheapest = []  # Contains the least expensive item
expensive = []  # Contains the most expensive item
product_details = []
all_product_details = []  # Contains all products and their details
too_expensive_id_list = [""]  # If an item's cost > the users money on hand,
# it will be added to this list

# Setting variables
global price
another_product = ""
recommended_purchase = ""
convert_to_grams = False
convert_to_litres = False
convert_to_kg = False
convert_to_ml = False

# Zeroing variables
mass = 0
count = 0
money = 0
product_entries = 0


# Abbreviation lists
ml = ["milliliter", "millilitre", "cc", "mL",
      "milliliters", "millilitres", "mls"]
litre = ["liter", "litre", "l", "liters", "litres"]
grams = ["g", "gram", "gms", "grams", "gm"]
kilograms = ["kg", "kilogram", "kilograms"]
all_units = [grams, kilograms, litre, ml]


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


# String checking function
def str_check(question, error):

    # Declaring global variables
    global convert_to_grams
    global convert_to_litres
    global convert_to_ml
    global convert_to_kg

    # Setting variables to false
    convert_to_grams = False
    convert_to_litres = False
    convert_to_kg = False
    convert_to_ml = False
    in_list = False
    valid = False

    while not valid:
        try:
            response = str(input(question)).lower().strip()
            for unit_list in all_units:
                if response in unit_list:
                    in_list = True
            # Checking if input is a valid unit
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
# Welcome + Information
print("                ******Welcome to the Product Comparer!******\n")
print("                ----------------Information----------------"
      "\nIf you are new to this program please feel free to read the following"
      " information.\nThe Product Comparer is a program that allows you to "
      "compare products to each other\n(e.g. a Small block of chocolate compar"
      "ed to a big block). The Product Comparer will\ndetermine which product "
      "is the best value in terms of price per mass/volume. The \nProduct "
      "Comparer will then make a recommendation on which product should be "
      "purchased,\nbased on the amount of money you are willing to spend and "
      "the value of the product.\n")
print("//Please enter the following details to proceed "
      "with the product comparisons\\\\ \n")

# Asking for money on hand
while money < 10:
    money = num_check("Please enter how much money you would like to spend: $",
                      "!!You must enter a number!!\n")
    if money < 10:
        print("!!You must have at least $10!!\n")

# Component 1
# Asking for details and doing error checking
while another_product.upper() != "YES":
    product_details = []
    another_product = ""

    product_details.append(blank_checker("\nEnter the product name: ",
                                         "!!You cannot leave this blank!!\n"))

    product_details.append(str_check("Enter the unit of measurement: ",
                                     "!!Enter a valid measurement (you cannot "
                                     "compare mass to volume)!!\n"))

    if convert_to_grams:
        product_details.append(num_check("Enter the product mass/volume: ",
                                         "!!Please enter a number "
                                         "above 0!!\n"))
        if litre in all_units:
            all_units.remove(litre)
            all_units.remove(ml)

    elif convert_to_kg:
        product_details.append(num_check("Enter the product mass/volume: ",
                                         "!!Please enter a number "
                                         "above 0!!\n")*1000)
        if litre in all_units:
            all_units.remove(litre)
            all_units.remove(ml)

    elif convert_to_litres:
        product_details.append(num_check("Enter the product mass/volume: ",
                                         "!!Please enter a number "
                                         "above 0!!\n")*1000)
        if grams in all_units:
            all_units.remove(grams)
            all_units.remove(kilograms)

    elif convert_to_ml:
        product_details.append(num_check("Enter the product mass/volume: ",
                                         "!!Please enter a number "
                                         "above 0!!\n"))
        if grams in all_units:
            all_units.remove(grams)
            all_units.remove(kilograms)

    product_details.append(num_check("Enter the product price: $",
                                     "!!Please enter a price above $0!!\n"))

    all_product_details.append(product_details)
    product_entries += 1

    if product_entries > 1:
        another_product = input("Would you like to compare the products yet? ")
        while another_product.upper().strip() != "NO" and \
                another_product.upper().strip() != "YES":
            another_product = input("!!Enter either 'Yes' or 'No'!!\nWould you"
                                    " like to compare the products yet? ")
    else:
        another_product = "NO"


# Component 2
# Extracting mass and price from all_product_details to get price_per_unit
for product in all_product_details:
    mass = 0
    price = 0
    count = 0
    for detail in product:
        if count == 2:
            mass = detail
        elif count == 3:
            price = detail
        count += 1

    if price > money:
        too_expensive_id_list.append(price)
        price = 0
        mass = 0
    else:
        price_per_unit = price / mass
        product.append(price_per_unit)
        price_per_unit_list.append(price_per_unit)

if len(price_per_unit_list) > 0:
    price_per_unit_list = sorted(price_per_unit_list)
    best_buy_price = price_per_unit_list[0]
    for product in all_product_details:
        if best_buy_price in product:
            recommended_purchase = product[0]
else:
    i = 0
    low_i = 0
    for product in all_product_details:
        if i == 0:
            lowest = product[3]/product[2]
        if product[3]/product[2] < lowest:
            lowest = product[3]/product[2]
            low_i = i
        i += 1
    recommended_purchase = "You can't afford any of these items but the " \
                           "best value item is {}"\
        .format(all_product_details[low_i][0])


# Component 3
# Ranking from most expensive to least expensive
for product in all_product_details:
    prices.append(product[3])

prices = sorted(prices)
prices = [prices[0], prices[-1]]
for product in all_product_details:
    for detail in product:
        for price in prices:
            if prices[0] in product:
                cheapest = product[0]
            if prices[-1] in product:
                expensive = product[0]


# Component 4 - summary
print("\n\n------Products Entered------\n")

# Extracting details from all_product_details
count = 0
for product in all_product_details:
    for detail in product:
        if count == 0:
            print("Item name: " + str(detail))
        elif count == 2:
            mass = detail
        elif count == 3:
            print("Cost: $" + str("{:.2f}".format(detail)))
            price = detail

        count += 1
        for ID in too_expensive_id_list:
            if str(ID) == str(price):
                if count == 4:
                    count = 0
            else:
                if count == 5:
                    count = 0

    price_per_unit = price / mass
    print("Average unit price: ${:.4f}\n".format(price_per_unit))

print("\n------Cheapest and Most Expensive Products------\n")
print("Cheapest Product: {}\nMost Expensive Product: {}\n".format
      (cheapest, expensive))

print("\n------Recommended Product Purchase in Terms of Value------\n")
print("Recommended Product Purchase (Best value affordable item): {}"
      .format(recommended_purchase))
