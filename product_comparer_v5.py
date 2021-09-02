""" Product Comparer - Full working program with changes made in relation to
feedback given in usability (adding extra measurements etc.)
Created by Sammy Cummins
Version 5
02/09/2021
"""

loop = "Yes"  # Allows program to run

# Abbreviation lists
ml = ["milliliter", "millilitre", "cc", "ml",
      "milliliters", "millilitres", "mls", False, 1]
litre = ["liter", "litre", "l", "liters", "litres", False, 1000]
grams = ["g", "gram", "gms", "grams", "gm", True, 1]
kilograms = ["kg", "kilogram", "kilograms", True, 1000]
ounce = ["ounce", "ounces", "oz", True, 28.34952]
pounds = ["pound", "pounds", "lb", "lbs", True, 453.59237]


# FUNCTIONS
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


def conversion(question, error):
    valid = False
    in_list = False
    while not valid:
        try:
            response = str(input(question)).lower().strip()
            for unit in all_units:
                for specific_unit in unit:
                    if response == specific_unit:
                        in_list = True
                        unit_type_mass = unit[-2]
                        conversion_factor = unit[-1]

            if in_list:
                product_details.append(num_check(
                    "Enter the product mass/volume: ",
                    "!!Please enter a number "
                    "above 0!!\n")*conversion_factor)
                if unit_type_mass is True and litre in all_units:
                    all_units.remove(litre)
                    all_units.remove(ml)
                    return response
                elif unit_type_mass is False and grams in all_units:
                    all_units.remove(grams)
                    all_units.remove(kilograms)
                    all_units.remove(ounce)
                    all_units.remove(pounds)
                    return response
                else:
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


# Main Routine
while loop != "NO":
    # List Declaration
    price_per_unit_list = []  # Contains the price/mass for each product
    price_per_unit = []
    prices = []
    all_units = [grams, kilograms, ounce,
                 pounds, litre, ml]  # Contains all unit lists
    cheapest = []  # Contains the least expensive item
    expensive = []  # Contains the most expensive item
    product_details = []
    all_product_details = []  # Contains all products and their details
    too_expensive_id_list = [""]  # If an item's cost > the users money on
    # hand, it will be added to this list

    # Setting variables
    global price
    another_product = ""
    recommended_purchase = ""

    # Zeroing variables
    mass = 0
    count = 0
    money = 0
    product_entries = 0

    # Asking for money on hand
    while money < 10:
        money = num_check("Please enter how much money you would like to "
                          "spend: $", "!!You must enter a number!!\n")
        if money < 10:
            print("!!You must have at least $10!!\n")

    # Component 1
    # Asking for details and doing error checking
    while another_product.upper() != "YES":
        product_details = []
        another_product = ""

        product_details.append(blank_checker("\nEnter the product name: ",
                                             "!!You cannot leave this "
                                             "blank!!\n"))

        product_details.append(conversion("Enter the unit of measurement: ",
                                          "!!Enter a valid measurement (you c"
                                          "annot compare mass to volume)!!\n"))

        product_details.append(num_check("Enter the product price: $",
                                         "!!Please enter a price "
                                         "above $0!!\n"))

        all_product_details.append(product_details)
        product_entries += 1

        if product_entries > 1:
            another_product = input("Would you like to compare the products "
                                    "yet? ")
            while another_product.upper().strip() != "NO" and \
                    another_product.upper().strip() != "YES":
                another_product = input("!!Enter either 'Yes' or 'No'!!\n"
                                        "Would you like to "
                                        "compare the products yet? ")
        else:
            another_product = "NO"

    # Component 2
    # Extracting mass and price from all_product_details to get price_per_unit
    for product in all_product_details:
        mass = 0
        price = 0
        count = 0
        for detail in product:
            if count == 1:
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
                lowest = product[3]/product[1]
            if product[3]/product[1] < lowest:
                lowest = product[3]/product[1]
                low_i = i
            i += 1
        recommended_purchase = "You can't afford any of these items but the " \
                               "best value item is {}"\
            .format(all_product_details[low_i][0])

    # Component 3
    # Ranking from most expensive to least expensive

    # Extracting all prices and appending them to prices list
    for product in all_product_details:
        prices.append(product[3])

    minimum = -1  # Holds the minimum price
    maximum = -1  # Holds the maximum price
    cheapest_list = []  # Holds cheapest prices
    expensive_list = []  # Holds most expensive prices
    cheapest = ""  # Holds name of cheapest product
    expensive = ""  # Holds name of most expensive product
    count_cheap = 1  # Keeps track of the number of products
    # that have the same cheapest price
    count_expensive = 1  # Keeps track of the number of products
    # that have the same expensive price

    # Deciding the max and min prices
    for product in all_product_details:
        for price in prices:
            if price <= minimum or minimum == -1:
                minimum = price
            if price >= maximum:
                maximum = price
        if product[3] == minimum:
            cheapest_list.append(product[3])
        if product[3] == maximum:
            expensive_list.append(product[3])

    for product in all_product_details:
        if cheapest_list[0] == product[3] and\
                not count_cheap > len(cheapest_list):
            # Formatting the cheapest products with spacing (", ")
            if count_cheap == len(cheapest_list):
                cheapest += product[0]
                count_cheap += 1
            else:
                cheapest += product[0] + ", "
                count_cheap += 1

        if expensive_list[0] == product[3] and \
                not count_expensive > len(expensive_list):
            # Formatting the most expensive products with spacing (", ")
            if count_expensive == len(expensive_list):
                expensive += product[0]
                count_expensive += 1
            else:
                expensive += product[0] + ", "
                count_expensive += 1

    # Component 4 - summary
    print("\n\n------Products Entered------\n")

    # Extracting details from all_product_details
    count = 0
    for product in all_product_details:
        price = product[3]
        mass = product[1]
        print("")
        print("Product name: " + product[0])
        print("Cost: ${:.2f}".format(price))

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

    loop = input("\n\nWould you like to use the program again? (Type 'Yes' to"
                 " use again or 'No' to exit): ").upper().strip()
    while loop.upper().strip() != "NO" and \
            loop.upper().strip() != "YES":
        loop = input("!!Enter either 'Yes' or 'No'!!\nWould you like to use "
                     "the program again? (Type 'Yes' to use again or 'No' to "
                     "exit): ")
