import json
from product import Product


def read_dataset(filename: str) -> list:
    products = list()
    with open(filename) as json_file:
        data = json.load(json_file)
        for data_product in data:
            product = Product(data_product['nombre'], data_product['precio'], data_product['descripcion'],
                              data_product['categoria'], data_product['marca'], data_product['colores'])
            products.append(product)
    return products

if __name__ == '__main__':
    filename = "datasets/products.json"
    products = read_dataset(filename)
