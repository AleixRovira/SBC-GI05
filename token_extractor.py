import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt_tab')

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    filtered = []
    for word in tokens:
        if word not in stopwords.words('english'):
            filtered.append(word)
    return filtered