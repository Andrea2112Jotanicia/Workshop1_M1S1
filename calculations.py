"""
Module responsible for calculating totals
"""

def calculate_sales(sales_list):

    product_totals = {}
    total_income = 0

    for sale in sales_list:

        product = sale["product"]
        price = sale["price"]
        quantity = sale["quantity"]

        sale_total = price * quantity
        total_income += sale_total

        if product in product_totals:
            product_totals[product] += quantity
        else:
            product_totals[product] = quantity

    return product_totals, total_income