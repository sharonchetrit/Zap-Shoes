import os, json
from product import Product


def add_json_to_db():
    root = os.path.realpath(os.path.dirname(__file__))
    path_to_file = os.path.join(root, 'static/data', 'products.json')

    with open(path_to_file, 'r') as f:
        products_data = json.load(f)
        for product_dict in products_data:
            product = Product(None, product_dict['name'], product_dict['price'], product_dict['image'],
                              product_dict['rating'])
            product.save_to_db()


add_json_to_db()
