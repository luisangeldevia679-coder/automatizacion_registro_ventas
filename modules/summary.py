def show_summary(product_summary, total_income):
    print("------------------------")
    print("SALES SUMMARY OF THE DAY")
    print("------------------------")

    for product, quantity in product_summary.items():
        print(f"Product: {product}")
        print(f"Total quantity sold: {quantity}")
    print(f"Total income: ${total_income}")