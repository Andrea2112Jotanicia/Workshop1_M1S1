"""
Module responsible for printing the final report
"""

from datetime import datetime


def print_summary(product_totals, total_income):

    date = datetime.now().strftime("%Y-%m-%d")

    print("\nSALES SUMMARY")
    print("Date:", date)
    print("-----------------------")

    for product in product_totals:

        print("Product:", product)
        print("Total quantity sold:", product_totals[product])
        print()

    print("Total income:", total_income)