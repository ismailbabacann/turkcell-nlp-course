#%%

import nltk
nltk.download("wordnet")

from nltk.stem import PorterStemmer

from nltk.stem import WordNetLemmatizer

lemmazer = WordNetLemmatizer()
stemmer = PorterStemmer()

#%% stem
words = ["running", "runner", "ran","runs","better","go","went"]

stems = [stemmer.stem(w) for w in words]
print("Stem Result: ", stems)

#%% lemma

words = ["running", "runner", "ran","runs","better","go","went"]
lemmas = [lemmazer.lemmatize(w , pos="v") for w in words]
print("Lemmas(anlamli):" , lemmas)
