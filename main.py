from modules.register import register_sale 
from modules.calculations import summarize_sales
from modules.summary import show_summary

def main():
    print("Sales system started")

    sales_list = []
    continue_registering = "yes"
    while continue_registering == "yes":
        sale = register_sale()
        sales_list.append(sale)

        continue_registering = input("Do you want to register another sale? (yes/no): ").lower()
    product_summary, total_income = summarize_sales(sales_list)
    show_summary(product_summary, total_income)
if __name__ == "__main__":
    main()

        