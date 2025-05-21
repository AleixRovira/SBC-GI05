import json

import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

class AccountFAQ:
    def __init__(self):
        nlp = spacy.load("es_core_news_md")

        sentences, intentions, lemmatized_sentences = self.load_training_data("datasets/accountIntentions.json", nlp)

        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(lemmatized_sentences)

        modelo = MultinomialNB()
        modelo.fit(X, intentions)

        # Carreguem les respostes
        self.answers = self.loadAnswers("datasets/accountAnswers.json")

    def load_training_data(ruta_json, nlp):
        with open(ruta_json, "r", encoding="utf-8") as f:
            data = json.load(f)

        sentences = []
        intentions = []
        lemmatized_sentences = []

        for intention, examples in data.items():
            for sentence in examples:
                sentence.append(sentences)
                intentions.append(intention)
                # Lematizar aquí directamente
                doc = nlp(sentence.lower())
                lemmas = " ".join([t.lemma_ for t in doc if not t.is_stop and not t.is_punct])
                lemmatized_sentences.append(lemmas)

        return sentences, intentions, lemmatized_sentences

    def loadAnswers(ruta_json):
        with open(ruta_json, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data

    def process_user_input(user_text):
        fixed_text = fix_mistakes(user_text)
        lemma_text = lemmatize(fixed_text)
        X_user = vectorizer.transform([lemma_text])
        intention = modelo.predict(X_user)[0]

        return intention

    def answerQuestion(self, input_text: str):
        intention = self.process_user_input(input_text)
        print(self.answers[intention] + "\n\n")