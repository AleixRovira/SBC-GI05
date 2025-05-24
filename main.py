import json

import spacy
import language_tool_python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from budget import Budget
from compare_products import CompareProducts
from product import Product
from replacement import Replacement
from token_extractor import tokenize
from availability import Availability


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


def fix_mistakes(texto):
    matches = tool.check(texto)
    return language_tool_python.utils.correct(texto, matches)


def lemmatize(texto):
    doc = nlp(texto.lower())
    lemmas = []
    for token in doc:
        if not token.is_stop and not token.is_punct:
            lemmas.append(token.lemma_)
    lemmatized_text = " ".join(lemmas)
    return lemmatized_text


def load_training_data(ruta_json, nlp):
    with open(ruta_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    sentences = []
    intentions = []
    lemmatized_sentences = []

    for intention, examples in data.items():
        for sentence in examples:
            sentences.append(sentence)
            intentions.append(intention)
            # Lematizar aquí directamente
            doc = nlp(sentence.lower())
            lemmas = " ".join([t.lemma_ for t in doc if not t.is_stop and not t.is_punct])
            lemmatized_sentences.append(lemmas)

    return sentences, intentions, lemmatized_sentences


def process_user_input(user_text):
    fixed_text = fix_mistakes(user_text)
    lemma_text = lemmatize(fixed_text)
    X_user = vectorizer.transform([lemma_text])
    intention = modelo.predict(X_user)[0]

    return intention


if __name__ == '__main__':
    filename = "datasets/products.json"
    products = read_dataset(filename)

    nlp = spacy.load("es_core_news_md")
    tool = language_tool_python.LanguageTool('es')

    sentences, intentions, lemmatized_sentences = load_training_data("datasets/intentions.json", nlp)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(lemmatized_sentences)

    modelo = MultinomialNB()
    modelo.fit(X, intentions)
    text = input("Soy GreenLandMXBot en que puedo ayudarte?\n")

    while True:
        intention = process_user_input(text)
        filtered_tokens = tokenize(text)
        
        if intention == "comparar_productos":
            cp = CompareProducts(products)
            cp.compare_products(text)
        elif intention == "hacer_presupuesto":
            budget = Budget(products)
            budget.checkInputForBudget(filtered_tokens)
        elif intention == "consultar_disponibilidad":
            availability = Availability(products)
            respuesta = availability.answer_availability(filtered_tokens)
            print(respuesta)
        elif intention == "informacion_producto":
            print("Intention: " + intention)
        elif intention == "seguimiento_pedido":
            print("Intention: " + intention)
        elif intention == "devolucion_producto":
            replacement_finder = Replacement(products, filtered_tokens)
            replacement_finder.find_replacement()
        elif intention == "recomendar_talla":
            print("Intention: " + intention)
        elif intention == "saludo":
            print("Hola! ¿En que te puedo ayudar?")
            continue
        elif intention == "despedida":
            print("¡Hasta la próxima!")
            break
        text = input("¿Necesitas algo más?\n")

