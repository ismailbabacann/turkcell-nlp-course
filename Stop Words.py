import nltk

from nltk.corpus import stopwords

nltk.download("stopwords")

#%%
stop_words= set(stopwords.words("english"))

#ornek 
text = "this is a example of removing stop words from text"
print(text)

filtered_words = [word for word in text.split()  if word.lower() not in stop_words]
print(filtered_words)

#%%

stop_words= set(stopwords.words("turkish"))

new_text = "bu cümle stopwords konusunu öğrenmek için sizlere yazılmıştır."
filtered_words2 = [word for word in new_text.split()  if word.lower() not in stop_words]

print(filtered_words2)

#%%
#kendi stopwordlerini ekleme

mystop_words= set(["ahmet","mehmet","için","sizlere","bu","o"])
new_text = "bu cümle stopwords konusunu öğrenmek için sizlere yazılmıştır."
filtered_words3 = [word for word in new_text.split()  if word.lower() not in mystop_words]

print(filtered_words3)
