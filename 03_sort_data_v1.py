""" Component 3 - Sort the user data into individual items and their details
Created by Sammy Cummins
Version 1
04/08/2021
"""
product_details = [['Potato', 'g', 200.0, 1.0],
                   ['Trampoline', 'kg', 100000.0, 300.0],
                   ['Pig', 'kg', 30000.0, 350.0]]

count = 0
item = []
for item in product_details:
    if count == 4:
        print("")
        count = 0
    for info in item:
        if count == 0:
            print("Item name: " + info)
        elif count == 1:
            print("Input unit: " + info)
        elif count == 2:
            print("Mass/volume (After conversion to smaller unit): "
                  + str(info))
        elif count == 3:
            print("Cost: $" + str(info))
        count += 1
