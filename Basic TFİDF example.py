from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

documents = [
    "kedi çok tatlı bir hayvandır.",
    "kedi ve köpek çok tatlı bir hayvanlardır.",
    "arılar bal üretirler"
 ]

tfidfvectorizer = TfidfVectorizer()


#metinleri sayısal veriye çevirme işlemi
X = tfidfvectorizer.fit_transform(documents)

#kelime kümesi
feature_names = tfidfvectorizer.get_feature_names_out()

print("tfidf vektör temsilleri")
vektortemsili= X.toarray()
print(vektortemsili)

df_tfidf = pd.DataFrame(vektortemsili, columns=feature_names)

kedi_tfidf = df_tfidf["kedi"]
kedi_mean_tfidf = np.mean(kedi_tfidf)
print(kedi_mean_tfidf)
