
class Abailability:
    def __init__(self, products):
        self.abailability = True
        self.products = products

    def get_abailability(self, name, brand, product, size, color, tokens) -> int:

        final_products = self.products.copy()

        for product in final_products:
            if not (name is None):
                if not(product.name in tokens):
                    final_products.remove(product)

        for product in final_products:
            if not (brand is None):
                if not(product.brand in tokens):
                    final_products.remove(product)

        for product in final_products:            
            if not (size is None):
                if not(product.size_availability[size] == 0):
                    final_products.remove(product)

        for product in final_products:
            if not (color is None):
                appears = 0
                for color in product.colors:
                    if color in tokens:
                        appears = 1
                        break
                if appears == 0:
                    final_products.remove(product)

        quantity = len(final_products)  

        return quantity
    
    def ask_abailability(self, tokens):
        categories = {"airbag", "glove", "pants", "jacket", "boot", "full suit", "helmet"}
        brands = {"Scorpion", "Sidi", "Spidi", "IXS", "Bell", "Schuberth", "Gaerne", "Held", "Dainese", "Modeka", "TCX", "Rukka", "Nolan", "Alpinestars", "Shoei", "RST", "Furygan", "Shark", "X-Lite", "LS2", "Klim", "Forma", "Macna", "AGV", "Revit", "Roviron", "Bering", "Icon", "Arai", "HJC"}
        colors = {"red", "blue", "green", "black", "white", "yellow", "orange", "purple", "pink", "gray", "brown"}
        sizes = ["xxxs", "xxs", "xs", "s", "m", "l", "xl", "xxl", "xxxl"]

        name = None
        brand = None
        category = None
        size = None
        color = None

        for token in tokens:
            token.lower()
            if token in brands:
                brand = token
            elif token in categories:
                category = token
            elif token in colors:
                color = token
            elif token in sizes:
                size = sizes.index(token)

        for product in self.products:
            if product.name in tokens:
                name = product.name
                break
        
        abailable_items = self.get_abailability(name, brand, category, size, color, tokens)
        print(f"There are {abailable_items} products that match your criteria.")
