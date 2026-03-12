def summarize_sales(sales_list):
    product_summary = {}
    total_income = 0

    for sale in sales_list:
        product = sale["product"]
        price = int(sale["price"])
        quantity = int(sale["quantity"])
        total = price * quantity
        product_summary[product] = product_summary.get(product, 0) + quantity
        total_income = total_income + total

    return product_summary, total_income