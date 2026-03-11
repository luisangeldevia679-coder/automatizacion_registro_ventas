def register_sale():
    """
    Capture sale information from user with validation
    """

    product = validate_product()
    price = validate_price()
    quantity = validate_quantity()

    sale = {
        "product": product,
        "price": price,
        "quantity": quantity
    }

    return sale


def validate_product():
    """
    Validate product name input
    """

    product = input("Enter product name: ").strip()

    while product == "":
        print("Error: Product name cannot be empty")
        product = input("Enter product name: ").strip()

    return product


def validate_price():
    """
    Validate price input
    """

    valid = False

    while valid == False:

        try:
            price = float(input("Enter unit price: "))

            if price <= 0:
                print("Error: Price must be greater than 0")
            else:
                valid = True

        except ValueError:
            print("Error: Please enter a valid number")

    return price


def validate_quantity():
    """
    Validate quantity input
    """

    valid = False

    while valid == False:

        try:
            quantity = int(input("Enter quantity sold: "))

            if quantity <= 0:
                print("Error: Quantity must be greater than 0")
            else:
                valid = True

        except ValueError:
            print("Error: Please enter a valid integer")

    return quantity