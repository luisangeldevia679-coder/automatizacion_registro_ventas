def register_sale():"""Registers sale information from user with validation"""

#Validate product name
product = ""
while product.strip() == "": product = input("Enter the product name: ")
if product.strip() == "":print("Product name cannot be empty. Please try again.")

