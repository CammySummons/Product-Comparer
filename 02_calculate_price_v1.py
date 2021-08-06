""" Component 2 - Calculate the average unit price (price/mass or volume) and
find the lowest price per unit mass/volume to be the recommended purchase
Created by Sammy Cummins
Version 1
30/07/2021
"""
all_product_details = [['Potato', 'g', 200.0, 1.0],
                   ['Trampoline', 'kg', 100000.0, 300.0],
                   ['Pig', 'kg', 30000.0, 350.0]]

product_no = 0
price_per_unit_list = []
price_per_unit = []
for product_details in all_product_details:
    mass = 0
    price = 0
    count = 0
    for info in product_details:
        if count == 2:
            mass = info
        elif count == 3:
            price = info
        count += 1

    product_no += 1
    price_per_unit = price / mass
    product_details.append(price_per_unit)
    price_per_unit_list.append(price/mass)
    print("Product no.{} price per unit mass/volume: {}".format
          (product_no, price_per_unit))

price_per_unit_list = sorted(price_per_unit_list)
best_buy_price = price_per_unit_list[0]

for product_details in all_product_details:
    if best_buy_price in product_details:
        print("Recommended Purchase: {}".format(product_details[0]))



