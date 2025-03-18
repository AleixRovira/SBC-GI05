import json
import nltk
from nltk.corpus import stopwords
from product import Product
from replacement import Replacement

nltk.download('stopwords')

def read_dataset(filename: str) -> list:
    products = list()
    with open(filename) as json_file:
        data = json.load(json_file)
        for data_product in data:
            product = Product(data_product['nombre'], data_product['precio'], data_product['descripcion'],
                              data_product['categoria'], data_product['marca'], data_product['colores'])
            products.append(product)
    return products

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    filtered = []
    for word in tokens:
        if word not in stopwords.words('english'):
            filtered.append(word)
    return filtered

if __name__ == '__main__':
    filename = "datasets/products.json"
    products = read_dataset(filename)
    text = input("Texto a tokenizar: ")
    filtered_tokens = tokenize(text)
    print("Filtered Tokens:", filtered_tokens)

    replacement_finder = Replacement(products)
    replacement_finder.find_replacement()