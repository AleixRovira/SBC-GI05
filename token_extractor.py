import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    filtered = []
    for word in tokens:
        if word not in stopwords.words('english'):
            filtered.append(word)
    return filtered