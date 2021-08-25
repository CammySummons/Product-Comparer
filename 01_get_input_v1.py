""" Component 1 - Get product details from user
Created by Sammy Cummins
Version 1
29/07/2021
"""

another_product = ""
product_details = []
all_product_details = []

# Main Routine
money = float(input("How much money would you like to spend? $"))

while another_product.upper() != "YES":
    product_details = []

    # Getting product details
    product_details.append(input("Enter the product name: "))
    product_details.append(str(input("Enter the unit of measurement: ")))
    product_details.append(float(input("Enter the product mass/volume: ")))
    product_details.append(float(input("Enter the product price: $")))

    all_product_details.append(product_details)

    another_product = input("Would you like to compare the products yet? ")
    while another_product.upper() != "NO" and another_product.upper() != "YES":
        another_product = input("!!Enter either 'Yes' or 'No'!!\n"
                                "Would you like to compare the products yet? ")

print(all_product_details)
