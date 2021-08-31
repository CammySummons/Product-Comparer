""" Component 2 - Calculate the average unit price (price/mass or volume) and
find the lowest price per unit mass/volume which is also affordable
to be the recommended purchase
Created by Sammy Cummins
Alternate version of version 2 that still reaches the same result
31/08/2021
"""

# Sample data which is hard coded but won't be when everything is compiled
all_product_details = [['Potato', 'g', 200.0, 1.0],
                       ['Trampoline', 'kg', 100000.0, 300.0],
                       ['Pig', 'kg', 30000.0, 350.0]]

price_per_unit_list = []
price_per_unit = []

money = float(input("How much money would you like to spend? $"))

# Extracting mass and price from all_product_details to get price_per_unit
for product in all_product_details:

    mass = product[2]
    price = product[3]
    name = product[0]

    # If the price of a product is more expensive than the amount you have, the
    # lower cost item overrides it, making the lower cost one more recommended
    if price > money:
        price = 0
        mass = 0
    else:
        price_per_unit = price / mass
        product.append(price_per_unit)
        price_per_unit_list.append(price_per_unit)
    print("{} price per unit mass/volume: {}".format
          (name, price_per_unit))

price_per_unit_list = sorted(price_per_unit_list)
best_buy_price = price_per_unit_list[0]

for product in all_product_details:
    if best_buy_price in product:
        recommended_purchase = product[0]
        print("Recommended Purchase: {}".format(recommended_purchase))
