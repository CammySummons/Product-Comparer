""" Component 3 - Sort the user data into individual items and their details
Get the cheapest and most expensive items
Created by Sammy Cummins
Version 1
04/08/2021
"""

# Sample data which is hard coded but won't be when everything is compiled
all_product_details = [['Potato', 'g', 200.0, 1.0],
                   ['Trampoline', 'kg', 100000.0, 300.0],
                   ['Pig', 'kg', 30000.0, 350.0]]
prices = []
cheapest = []
expensive = []

# Ranking from most expensive to least
for i in all_product_details:
    prices.append(i[3])

prices = sorted(prices)
prices = [prices[0], prices[-1]]
for product in all_product_details:
    for detail in product:
        for price in prices:
            if prices[0] in product:
                cheapest = product[0]
            elif prices[1] in product:
                expensive = product[0]

print("Cheapest Item:  {}\nMost Expensive Item: {}\n".format(cheapest, expensive))

# Printing products and their information
# print("--Product Information--")
# count = 0
# item = []
# for item in all_product_details:
#     if count == 4:
#         print("")
#         count = 0
#     for info in item:
#         if count == 0:
#             print("Item name: " + info)
#         elif count == 1:
#             print("Input unit: " + info)
#         elif count == 2:
#             print("Mass/volume (After conversion to smaller unit): "
#                   + str(info))
#         elif count == 3:
#             print("Cost: $" + str(info))
#         count += 1
