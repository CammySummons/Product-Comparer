""" Component 2 - Calculate price per unit
Created by Sammy Cummins
Version 1
30/07/2021
"""
product_details = [['Potato', 'g', 200.0, 1.0],
                   ['Trampoline', 'kg', 100000.0, 300.0],
                   ['Pig', 'kg', 30000.0, 350.0]]

product_no = 0
price_per_unit = []
for item in product_details:
    mass = 0
    price = 0
    count = 0
    for info in item:
        if count == 2:
            mass = info
        elif count == 3:
            price = info
        count += 1

    product_no += 1
    price_per_unit = price / mass
    print("Product no.{} price per unit mass/volume: {}".format
          (product_no, price_per_unit))
