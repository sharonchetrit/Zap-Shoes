import os, json
from product import Product
from user import User
from database import connect
from flask import request


def get_products():
    products = []
    with connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM products")
            products_data = cursor.fetchall()
            for product_data in products_data:
                product = Product(id=product_data[0], price=product_data[1], name=product_data[2],
                                  image=product_data[3], rating=product_data[4])
                products.append(product)

    return products


def get_product(product_id):
    with connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM products WHERE id=%s", (product_id,))
            product_data = cursor.fetchone()
            product = Product(id=product_data[0], price=product_data[1], name=product_data[2],
                              image=product_data[3], rating=product_data[4])

            return product

def get_user():
    users = []
    with connect() as connection:
        with connection.cursor as cursor:
            cursor.execute("SELECT * FROM users")
            users_data = cursor.fetchall()
            for user_data in users_data:
                user = User(id=user_data[0],)

