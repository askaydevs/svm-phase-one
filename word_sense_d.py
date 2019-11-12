import nltk
import codecs
from nltk.tokenize import PunktSentenceTokenizer, sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer, PorterStemmer

def simpleFilter(sentence):
    filtered_sent = []
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            filtered_sent.append(lemmatizer.lemmatize(w))

    return filtered_sent

def similarity_check(word1, word2):
    word1 = word1 + ".n.01"
    word2 = word2 + ".n.02"
    try:
        w1 = wordnet.sysnet(word1)
        w2 = wordnet.sysnet(word2)
        return w1.wup_similarity(w2)
    except:
        return 0

def synonymsCreator(word):
    synonyms = []
    for syn in wordnet.sysnets(word):
        for i in sys.lemmas():
            synonyms.append(i.name())
    return synonyms

def filteredSentence(sentence):
    filtered_sent = []
    lemmatizer = WordNetLemmatizer()
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            filtered_sent.append(lemmatizer.lemmatize(ps.stem(w)))
            for i in synonymsCreator(w):
                filtered_sent.append(i)

    return filtered_sent

print(similarity_check('dog', 'bitch'))    
