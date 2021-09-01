""" Component 4 - Display Results
Created by Sammy Cummins
Alternate version of version 1 that still reaches the same result
(by using dictionaries instead of lists)
01/09/2021
"""

# Sample data which is hard coded but won't be when everything is compiled
name_dict = {1: "Potato",
             2: "Trampoline",
             3: "Pig"}

mass_dict = {1: "200.0",
             2: "100000.0",
             3: "30000.0"}

price_dict = {1: "1.0",
              2: "300.0",
              3: "350.0"}

unit_dict = {1: "g",
             2: "kg",
             3: "kg"}

product_dict = {"name": name_dict,
                "mass": mass_dict,
                "price": price_dict,
                "unit": unit_dict}

# More sample data
cheapest = "Potato"
expensive = "Pig"
recommended_product = "Trampoline"

# Triggering summary with expected input
information_question = input("Enter Yes: ")

if information_question == "Yes":

    # Extracting details from all_product_details
    for name in name_dict:
        print("Item name: " + product_dict["name"][name])
        print("Cost: $" + product_dict["price"][name])
        price_per_unit = float(product_dict["price"][name]) / float(product_dict["mass"][name])
        print("Average unit price: ${:.4f}\n".format(price_per_unit))

    print("Cheapest Product: {}\nMost Expensive Product: {}\n".format
          (cheapest, expensive))
    print("Recommended Product Purchase (Best value and affordable item: {}"
          .format(recommended_product))
