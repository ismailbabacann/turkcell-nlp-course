from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "Kedi evde",
    "Kedi bahçede"
    ]

vectorizer= CountVectorizer()

x = vectorizer.fit_transform(documents)
print("kelime kümesi: ", vectorizer.get_feature_names_out())

print("vektör temsili: ", x.toarray())

"""
kelime kümesi:  ['bahçede' 'evde' 'kedi']
vektör temsili:  [[0 1 1]
 [1 0 1]]
"""