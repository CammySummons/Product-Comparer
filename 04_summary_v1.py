""" Component 4 - Display Results
Created by Sammy Cummins
Version 1
05/08/2021
"""

# Sample data which is hard coded but won't be when everything is compiled
all_product_details = [['Potato', 'g', 200.0, 1.0],
                   ['Trampoline', 'kg', 100000.0, 300.0],
                   ['Pig', 'kg', 30000.0, 350.0]]

# More sample data
cheapest = ["Potato"]
for i in cheapest:
    cheapest = i
expensive = ["Pig"]
for i in expensive:
    expensive = i
recommended_product = "Trampoline"

# Zeroing variables
mass = 0
price = 0

# Triggering summary with expected input
information_question = input("Enter Yes: ")

if information_question == "Yes":
    count = 0
    item = []

    # Extracting details from all_product_details
    for item in all_product_details:
        if count == 4:
            print("")
            count = 0
        for info in item:
            if count == 0:
                print("Item name: " + info)
            elif count == 2:
                mass = info
            elif count == 3:
                print("Cost: $" + str(info))
                price = info
            count += 1

        price_per_unit = price / mass
        price_per_unit = round(price_per_unit, 4)
        print("Average unit price: {}\n".format(price_per_unit))

    print("Cheapest Product: {}\nMost Expensive Product: {}\n".format
          (cheapest, expensive))
    print("Recommended Product Purchase (Best value and affordable item: {}"
          .format(recommended_product))
