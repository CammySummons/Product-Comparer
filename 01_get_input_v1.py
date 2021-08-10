""" Component 1 - Get product details from user
Created by Sammy Cummins
Version 1
29/07/2021
"""

another_product = ""


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


product_details = []
all_product_details = []

# Main Routine
money = float(input("How much money would you like to spend? $"))
while money < 10:
    money = float(input("!!You must have at least $10!!\nPlease "
                        "enter how much money you would like to spend: $"))

while another_product.upper() != "YES":
    product_details = []
    product_details.append(input("Enter the product name: "))
    product_details.append("Enter the unit of measurement: ")
    product_details.append("Enter the product mass/volume: ")
    product_details.append(num_check("Enter the product price: $",
                                     "!!Please enter a price above $0!!"))

    all_product_details.append(product_details)

    another_product = input("Would you like to compare the products yet? ")
    while another_product.upper() != "NO" and another_product.upper() != "YES":
        another_product = input("!!Enter either 'Yes' or 'No'!!\n"
                                "Would you like to compare the products yet? ")

print(all_product_details)
