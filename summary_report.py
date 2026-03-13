"""
Module responsible for printing the final report
"""

def print_summary(product_totals, total_income):

    print("\nSALES SUMMARY")
    print("-----------------------")

    for product in product_totals:

        print("Product:", product)
        print("Total quantity sold:", product_totals[product])
        

    print("Total income:", total_income)