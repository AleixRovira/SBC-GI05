import json

from budget import Budget
from product import Product
from replacement import Replacement
from token_extractor import tokenize

def read_dataset(filename: str) -> list:
    products = list()
    with open(filename) as json_file:
        data = json.load(json_file)
        for data_product in data:
            product = Product(data_product['nombre'], data_product['precio'], data_product['descripcion'],
                              data_product['categoria'], data_product['marca'], data_product['colores'],
                              data_product['dispo_tallas'])
            products.append(product)
    return products

if __name__ == '__main__':
    filename = "datasets/products.json"
    products = read_dataset(filename)

    while True:
        text = input("I am *IA name* what can I help you with? ")
        filtered_tokens = tokenize(text)
        print("Filtered Tokens:", filtered_tokens)

        if "thanks" in filtered_tokens:
            print("You're welcome! Have a great day!")
            break

        if "replacement" in filtered_tokens:
            replacement_finder = Replacement(products, filtered_tokens)
            replacement_finder.find_replacement()
        elif "compare" in filtered_tokens:
            a = 1 #Aqui va buestra clase quitar la linea
        elif "budget" in filtered_tokens:
            budget = Budget(products)
            budget.checkInputForBudget(filtered_tokens)
        elif "disponibility" in filtered_tokens:
            a = 1  # Aqui va buestra clase quitar la linea
        else:
            print("I'm sorry, I didn't understand your request.")