import re

class Budget:
    # Regex
    REGEX_BUDGET = r"(budget)\w*"
    CATEGORIES = [r"(airbag)\w*", r"(boot)\w*", r"(helmet)\w*", r"(jacket)\w*", r"(glove)\w*", r"(pant)\w*", r"(suit)\w*"]
    CATEGORY_NAMES = ["airbag", "boot", "helmet", "jacket", "glove", "pants", "full suit"]
    REGEX_CATEGORIES = rf"({'|'.join(CATEGORIES)})"

    non_categories = True
    wanted_categories = [False, True, True, True, True, True, False]  # Default categories
    category_products = {}

    def __init__(self, products: list):
        self.products = products.sort(key=lambda product: product.price)
        for product in products:
            if product.category not in self.category_products:
                self.category_products[product.category] = []
            self.category_products[product.category].append(product)

    def budgetWithoutCategory(self):
        print("Proposed budgets:")
        # Printar budget alta gamma
        total_sum = 0
        print("\n\tHigh range:")
        for i in range(0, len(self.CATEGORIES)):
            if self.wanted_categories[i]:
                index = len(self.category_products[self.CATEGORY_NAMES[i]]) - 1
                total_sum += self.category_products[self.CATEGORY_NAMES[i]][index].price
                print(f" - {self.CATEGORY_NAMES[i].upper()}: {self.category_products[self.CATEGORY_NAMES[i]][index].name} ({self.category_products[self.CATEGORY_NAMES[i]][index].price}€)")
        print(f"\nTotal price: {round(total_sum, 2)}")

        # Printar budget mitja gamma
        total_sum = 0
        print("\n\tMid renge:")
        for i in range(0, len(self.CATEGORIES)):
            if self.wanted_categories[i]:
                index = (len(self.category_products[self.CATEGORY_NAMES[i]]) - 1) // 2
                total_sum += self.category_products[self.CATEGORY_NAMES[i]][index].price
                print(f" - {self.CATEGORY_NAMES[i].upper()}: {self.category_products[self.CATEGORY_NAMES[i]][index].name} ({self.category_products[self.CATEGORY_NAMES[i]][index].price}€)")
        print(f"\nTotal price: {round(total_sum, 2)}")

        # Printar budget baixa gamma
        total_sum = 0
        print("\n\tLow range:")
        for i in range(0, len(self.CATEGORIES)):
            if self.wanted_categories[i]:
                total_sum += self.category_products[self.CATEGORY_NAMES[i]][0].price
                print(f" - {self.CATEGORY_NAMES[i].upper()}: {self.category_products[self.CATEGORY_NAMES[i]][0].name} ({self.category_products[self.CATEGORY_NAMES[i]][0].price}€)")
        print(f"\nTotal price: {round(total_sum, 2)}")

        # Preguntar la quantitat de diners que es vol gastar
        print("\nFor a more accurated range tell me your budget or the things you want to include\n")
        return

    def budgetWithCategories(self, budget: float):
        # Buscar amb busqueda binaria la millor combinacio
        # Busquem el index amb el budget adequat

        # Calculem el minim budget possible
        min_budget = 0
        for i in range(0, len(self.CATEGORIES)):
            if self.wanted_categories[i]:
                min_budget += self.category_products[self.CATEGORY_NAMES[i]][0].price

        if budget < min_budget:
            print("The budget is very low for the products you want, this is the cheapest combination:")
            total_sum = 0
            for i in range(0, len(self.CATEGORIES)):
                if self.wanted_categories[i]:
                    total_sum += self.category_products[self.CATEGORY_NAMES[i]][0].price
                    print(f" - {self.CATEGORY_NAMES[i].upper()}: {self.category_products[self.CATEGORY_NAMES[i]][0].name} ({self.category_products[self.CATEGORY_NAMES[i]][0].price}€)")
            print(f"\nTotal price: {round(total_sum, 2)}")
            return

        max_budget = 0
        for i in range(0, len(self.CATEGORIES)):
            if self.wanted_categories[i]:
                max_budget += self.category_products[self.CATEGORY_NAMES[i]][len(self.category_products[self.CATEGORY_NAMES[i]]) - 1].price

        # Busquem binariament el budget indicat
        total_sum = max_budget + 1
        por = 100
        while total_sum > budget and por >= 0:
            total_sum = 0
            for i in range(0, len(self.CATEGORIES)):
                if self.wanted_categories[i]:
                    index = ((len(self.category_products[self.CATEGORY_NAMES[i]]) - 1) * por) // 100
                    total_sum += self.category_products[self.CATEGORY_NAMES[i]][index].price
            if total_sum > budget:
                por -= 10

        total_sum = 0
        for i in range(0, len(self.CATEGORIES)):
            if self.wanted_categories[i]:
                index = ((len(self.category_products[self.CATEGORY_NAMES[i]]) - 1) * por) // 100
                total_sum += self.category_products[self.CATEGORY_NAMES[i]][index].price
                print(f" - {self.CATEGORY_NAMES[i].upper()}: {self.category_products[self.CATEGORY_NAMES[i]][index].name} ({self.category_products[self.CATEGORY_NAMES[i]][index].price}€)")
        print(f"\nTotal price: {round(total_sum, 2)}")

        return

    def checkInputForBudget(self, tokens: list):
        budget = -1
        for token in tokens:
            if self.non_categories and re.match(self.REGEX_CATEGORIES, token):
                self.non_categories = False
                for i in range(0, len(self.wanted_categories)):
                    self.wanted_categories[i] = False
            for i in range(0, len(self.CATEGORIES)):
                if re.match(self.CATEGORIES[i], token):
                    self.wanted_categories[i] = True
            # Si hi ha un numero significa que es la quantitat de diners
            if re.match(r"^\d+([.,]\d+)?", token):
                budget = float(token.replace(',', '.'))

        # Depenent de si s'han introduit
        if self.non_categories and budget < 0:
            self.budgetWithoutCategory()
        else:
            self.budgetWithCategories(budget)
        return
