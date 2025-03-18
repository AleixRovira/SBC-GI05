from token_extractor import tokenize

class Replacement:
    def __init__(self, products: list, token_list: list):
        self.products = products
        self.token_list = token_list

    def extract_filters(self):
        categories = {"airbags", "botas"}
        brands = {"fox", "leatt"}
        colors = {"red", "blue", "green", "black", "white", "yellow", "orange", "purple", "pink", "gray", "brown"}

        category = next((word for word in self.token_list if word.lower() in categories), None)
        brand = next((word for word in self.token_list if word.lower() in brands), None)
        max_price = None
        color = next((word for word in self.token_list if word.lower() in colors), None)

        for i in range(len(self.token_list) - 1):
            if self.token_list[i].isdigit() and self.token_list[i + 1].lower() in {"$", "dollars", "dollar"}:
                max_price = float(self.token_list[i])
                break

        if category is None:
            category = self.ask_user("¿Quiere su producto de alguna categoría en específico?", categories)
        if brand is None:
            brand = self.ask_user("¿Quiere su producto de alguna marca en específico?", brands)
        if max_price is None:
            max_price = self.ask_price()
        if color is None:
            color = self.ask_user("¿Quiere su producto de algún color en específico?", colors)

        return category, brand, max_price, color

    def ask_user(self, question, valid_options):
        response = input(question + " ")
        tokens = tokenize(response)
        return next((word for word in tokens if word.lower() in valid_options), None)

    def ask_price(self):
        response = input("Do you have in mind any maximum price? ")
        tokens = tokenize(response)
        for i in range(len(tokens) - 1):
            if tokens[i].isdigit() and tokens[i + 1].lower() in {"$", "dollars", "dollar"}:
                return float(tokens[i])
        return float('inf')

    def find_replacement(self):
        category, brand, max_price, color = self.extract_filters()

        filtered_products = [p for p in self.products
                             if (category is None or p.category.lower() == category.lower())
                             and (brand is None or p.brand.lower() == brand.lower())
                             and p.price <= max_price
                             and (color is None or color.lower() in map(str.lower, p.colors))]

        if filtered_products:
            print("Productos disponibles:")
            for p in filtered_products:
                print(f"{p.name} - ${p.price} - {p.colors}")
        else:
            print("No se encontraron productos con esos criterios.")