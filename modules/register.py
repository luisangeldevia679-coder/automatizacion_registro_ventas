def register_sale():

    product = input("Enter the product name: ")
    price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity sold: "))

    sale = {
        "product": product,
        "price": price,
        "quantity": quantity,
    }

    return sale