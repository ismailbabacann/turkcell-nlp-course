import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


df = pd.read_csv("spam.csv", encoding="ISO-8859-1")
df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis = 1, inplace= True)
df.columns= ["type","text"]

#tfidf
vectorizer = TfidfVectorizer(stop_words="english") # ben ayrıca stopwords ekledim
X = vectorizer.fit_transform(df["text"])

#kelime kümesi
feature_names = vectorizer.get_feature_names_out()
tfidf_score = X.mean(axis=0).A1 # ortalama tf-idf değerleri

df_tfidf = pd.DataFrame({
    "word": feature_names,
    "tfidf_score": tfidf_score
})

sorted_tfidf = df_tfidf.sort_values(by="tfidf_score", ascending=False)
print(sorted_tfidf)