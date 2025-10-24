import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re 
from collections import Counter
from nltk.corpus import stopwords

df = pd.read_csv("IMDB Dataset.csv")

#metin verilerini alma
documents = df["review"]
labels = df["sentiment"] #positive olanlar lazım


#metin temizleme fonskyionu
def clean_text(text):
    stop_words= set(stopwords.words("english"))

    text = text.lower() # kücük harfa cevirme
    
    text = re.sub(r"\d+", "", text) # rakamları temizleme
    
    text = re.sub(r"[^\w\s]", "", text)
    
    
    #homework stopwords ekleme
    text = " ".join([word for word in text.split() if word.lower() not in stop_words])

    
    text = " ".join([word for word in text.split() if len(word) > 2]) # kısa kelimeleri temizleme
    
    return text

#fonskyionu kullanarak metni temizleme
cleaned_documents = [clean_text(doc) for doc in documents]
    
# bow

vectorizer = CountVectorizer()

x = vectorizer.fit_transform(cleaned_documents[:100])
feature_names = vectorizer.get_feature_names_out()

print("vektör temsili")
vektor_temsili_2 = x.toarray()[:2]
print(vektor_temsili_2)

df_bow = pd.DataFrame(x.toarray(), columns= feature_names)

#kelime frekansı
word_counts = x.sum(axis= 0).A1
word_freq = dict(zip(feature_names, word_counts))

#ilk 5 kelime
most_common_words = Counter(word_freq).most_common(5)
print(most_common_words)




