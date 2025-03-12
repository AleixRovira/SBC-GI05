from product import Product
import json
import re

class Budget:
    # Regex
    REGEX_BUDGET = r"\b(presupuest)\w*\b"
    CATEGORIES = ["airbag", "bota", "casco", "chaqueta", "guante", "pantalone", "trajes\scompleto"]
    REGEX_CATEGORIES = rf"\b({'|'.join(CATEGORIES)})\b"
    REGEX_NEGATIONS = [r"(no|sin)"]

    # Regular expression pattern explanation:
    # - "\b(?:{REGEX_NEGATIONS})": Matches a negation word at the beginning.
    # - "(?!\s+\b{REGEX_BUDGET}\b)": Negative lookahead to ensure REGEX_BUDGET does NOT appear immediately after the negation.
    # - "(?:\s+\w+)*?": Allows any number of words between the negation and the category.
    # - "\s+\b{REGEX_CATEGORIES}\b": Matches the target category words.
    REGEX_INVERT_CATEGORIES = rf"\b(?:{REGEX_NEGATIONS})\b(?!\s+\b{REGEX_BUDGET}\b)(?:\s+\w+)*?\s+\b{REGEX_CATEGORIES}\b"

    default_categories = [False, True, True, True, True, True, False]    # Default categories
    category_products = {}

    def __init__(self, products: list):
        self.products = products
        for product in products:
            if product.category not in self.category_products:
                self.category_products[product.category] = []
            self.category_products[product.category].append(product)

    # TODO Esquema:
    # TODO Mirar si en l'input introduit s'ha introduit la paraules REGEX_BUDGET
    # TODO Mirar si s'ha introduit una quantitat
    # TODO Mirar si s'ha introduit un color en especific
    # TODO Mirar si s'han introduit productes en especial, sino utilitzar DEFAULT_BUDGET_CATEGORIES

    # Check if the regex REGEX_BUDGET appears
    def checkPresupost(self):
        return

    # Check what categories the user wants
    def checkCategories(self, input: str):
        # Detect all mentioned categories
        found_categories = re.findall(self.REGEX_CATEGORIES, input, re.IGNORECASE)

        # Check which ones are negated correctly
        confirmed_categories = set(found_categories)

        for category in found_categories:
            # Create a regex to check if the category has a negation just before, without another category or presupuesto in between
            negation_pattern = rf"{self.REGEX_NEGATIONS}(?!.*({self.REGEX_BUDGET}|{self.REGEX_CATEGORIES})).*?\b{category}\b"

            if re.search(negation_pattern, input, re.IGNORECASE):
                confirmed_categories.discard(category)  # Remove it if negated

        print(f"Sentence: {input}")
        print(f"Confirmed categories: {list(confirmed_categories)}\n")

    # TODO: Using a greedy algorithm, make the budget proposal
    # def makeBudget(self):

# TODO: Part a fer conjunta entre tots:
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
    bg = Budget(products)
    input_string = input("¡Hola! ¿En qué puedo ayudarte? ")
    bg.checkInputForBudget(input_string.lower())