def calculate_sale_total(price, quantity):
    return price * quantity

def summarize_sales(sales_list):

    product_summary = {}
    total_income = 0

    for sale in sales_list:
        product = sale["product"]
        price = sale["price"]
        quantity = sale["quantity"]

        total_income += calculate_sale_total(price, quantity)

        if product not in product_summary:
            product_summary[product] += quantity
        else:
            product_summary[product] = quantity

    return product_summary, total_income