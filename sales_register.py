"""
Module responsible for sales registration
"""

from input_validation import validate_string, validate_float, validate_integer


def register_sale():

    product = validate_string("Enter product name: ")
    price = validate_float("Enter unit price: ")
    quantity = validate_integer("Enter quantity sold: ")

    sale = {
        "product": product,
        "price": price,
        "quantity": quantity
    }

    return sale