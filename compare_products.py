from product import Product
import json
class CompareProducts:
    def __init__(self, products: list):
        self.products = products
        self.categories = list()
        for product in products:
            if product.category.lower() not in self.categories:
                self.categories.append(product.category.lower())


    def compare_products(self, input_string: str) -> None:
        compare_categories = False
        for category in self.categories:
            if category in input_string.lower():
                # Compare all products in that category
                compare_categories = True
                print(f"Para la categoria {category} tenemos los siguientes productos: ")
                print("{0:60}{1:20}{2:20}{3:20}".format("NOMBRE", "PRECIO", "MARCA", "COLORES"))
                for product in self.products:
                    if product.category.lower() == category:
                        formatted_colors = '/'.join(product.colors)
                        print("{0:60}{1:<20}{2:20}{3:20}".format(product.name, f"{product.price}€", product.brand, formatted_colors))

        product_1, product_2 = None, None
        if not compare_categories:
            for product in self.products:
                if product.name.lower() in input_string.lower():
                    if product_1 is None:
                        product_1 = product
                    else:
                        product_2 = product

        if product_1 is not None and product_2 is not None:
            # Compare products
            print("NOMBRE - PRECIO - MARCA - COLORES")
            formatted_colors_1 = '/'.join(product_1.colors)
            formatted_colors_2 = '/'.join(product_2.colors)
            print("{0:60}{1:<20}{2:20}{3:20}".format(product_1.name, f"{product_1.price}€", product_1.brand, formatted_colors_1))
            print("{0:60}{1:<20}{2:20}{3:20}".format(product_2.name, f"{product_2.price}€", product_2.brand, formatted_colors_2))

        if not compare_categories and product_1 is None and product_2 is None:
            # Error, does not want to compare products and does not want to compare category
            print("Perdona, no me has proporcionado una categoría o 2 productos para comparar, necesito esa información para poder ayudarte")


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
    cp = CompareProducts(products)
    input_string = input("¡Hola! ¿En qué puedo ayudarte? ")
    cp.compare_products(input_string)