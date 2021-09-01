""" Component 4 - Display Results
Created by Sammy Cummins
Version 2 - More efficient code
05/08/2021
"""

# Sample data which is hard coded but won't be when everything is compiled
all_product_details = [['Potato', 'g', 200.0, 1.0],
                   ['Trampoline', 'kg', 100000.0, 300.0],
                   ['Pig', 'kg', 30000.0, 350.0]]

# More sample data
cheapest = "Potato"
expensive = "Pig"
recommended_product = "Trampoline"

# Triggering summary with expected input
information_question = input("Enter Yes: ")

if information_question == "Yes":

    # Extracting details from all_product_details
    for product in all_product_details:
        price = product[3]
        mass = product[2]
        print("")
        print("Product name: " + product[0])
        print("Cost: $" + str(price))

        price_per_unit = price / mass
        print("Average unit price: ${:.4f}\n".format(price_per_unit))

    print("Cheapest Product: {}\nMost Expensive Product: {}\n".format
          (cheapest, expensive))
    print("Recommended Product Purchase (Best value and affordable item: {}"
          .format(recommended_product))
