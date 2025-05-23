
class Availability:
    def __init__(self, products):
        self.availability = True
        self.products = products

    def get_availability(self, name, brand, category, size, color, tokens) -> int:

        final_products = self.products.copy()

        remove_products = []

        for product in final_products:
            if not (name is None):
                if not(product.name in tokens):
                    remove_products.append(product)

        for product in remove_products:
            final_products.remove(product)

        remove_products = []

        for product in final_products:
            if not (brand is None):
                if not(product.brand in tokens):
                    remove_products.append(product)

        for product in remove_products:
            final_products.remove(product)
        
        remove_products = []

        for product in final_products:
            if not (category is None):
                if not(product.category in tokens):
                    remove_products.append(product)

        for product in remove_products:
            final_products.remove(product)

        remove_products = []

        for product in remove_products:
            final_products.remove(product)

        for product in final_products:            
            if not (size is None):
                if product.size_availability[size] == 0:
                    remove_products.append(product)

        for product in remove_products:
            final_products.remove(product)

        remove_products = []

        for product in final_products:
            if not (color is None):
                appears = 0
                for color in product.colors:
                    if color in tokens:
                        appears = 1
                        break
                if appears == 0:
                    remove_products.append(product)

        for product in remove_products:
            final_products.remove(product)

        quantity = len(final_products)  

        return quantity
    
    def answer_availability(self, tokens):
        categories = {"airbag", "airbags", "glove", "gloves", "pant", "pants", "jacket", "jackets", "boot", "boots", "full suit", "helmet", "helmets"}
        brands = {"Scorpion", "Sidi", "Spidi", "IXS", "Bell", "Schuberth", "Gaerne", "Held", "Dainese", "Modeka", "TCX", "Rukka", "Nolan", "Alpinestars", "Shoei", "RST", "Furygan", "Shark", "X-Lite", "LS2", "Klim", "Forma", "Macna", "AGV", "Revit", "Roviron", "Bering", "Icon", "Arai", "HJC"}
        colors = {"red", "blue", "green", "black", "white", "yellow", "orange", "purple", "pink", "gray", "brown"}
        sizes = ["xxxs", "xxs", "xs", "s", "m", "l", "xl", "xxl", "xxxl"]

        name = None
        brand = None
        category = None
        size = None
        color = None

        for token in tokens:
            t = token.lower()
            if t in brands:
                brand = t
            elif t in categories:
                category = t
            elif t in colors:
                color = t
            elif t in sizes:
                size = t

        for product in self.products:
            if product.name.lower() in [tok.lower() for tok in tokens]:
                name = product.name
                break

        available_items = self.get_availability(name, brand, category, size, color, tokens)

        if available_items > 0:
            return f"Sí, tenemos {available_items} producto(s) que cumplen tus criterios."
        else:
            return "Lo siento, no tenemos productos que cumplan esos criterios en este momento."
