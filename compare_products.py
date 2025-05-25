

class CompareProducts:
    def __init__(self, products: list, translated_categories, translated_colors):
        self.products = products
        self.categories = list()
        for product in products:
            if product.category.lower() not in self.categories:
                self.categories.append(product.category.lower())
        self.translated_categories = translated_categories
        self.translated_colors = translated_colors

    def compare_products(self, input_string: str) -> None:
        product_1, product_2 = None, None
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
            print("{0:30}{1:<20}{2:20}{3:20}".format(product_1.name, f"{product_1.price}€", product_1.brand, formatted_colors_1))
            print("{0:30}{1:<20}{2:20}{3:20}".format(product_2.name, f"{product_2.price}€", product_2.brand, formatted_colors_2))
            return

        for category in self.categories:
            if self.translated_categories[category] in input_string.lower():
                # Compare all products in that category
                compare_categories = True
                print(f"Para la categoría {self.translated_categories[category]} tenemos los siguientes productos:")
                print("{0:30}{1:20}{2:20}{3:20}".format("NOMBRE", "PRECIO", "MARCA", "COLORES"))
                for product in self.products:
                    if product.category.lower() == category:
                        formatted_colors = '/'.join(product.colors)
                        print("{0:30}{1:<20}{2:20}{3:20}".format(product.name, f"{product.price}€", product.brand, formatted_colors))
                return

        # Error, does not want to compare products and does not want to compare category
        print("Lo siento, no me has proporcionado una categoría o 2 productos para comparar,\nnecesito esa información para poder ayudarte.")