"""
Main controller of the application
"""

from welcome import show_welcome
from sales_register import register_sale
from calculations import calculate_sales
from summary_report import print_summary
from control import continue_register


def main():

    show_welcome()

    sales_list = []

    continue_program = True

    while continue_program:

        sale = register_sale()

        sales_list.append(sale)

        continue_program = continue_register()

    product_totals, total_income = calculate_sales(sales_list)

    print_summary(product_totals, total_income)


if __name__ == "__main__":
    main()