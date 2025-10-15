#%%nltk kullanarak tokenizasyon yapma

import nltk

nltk.download("punkt")
nltk.download("punkt_tab")

#%%
text = "Hello,World!  How ARE YOU?"

#kelimeleri tokenlere ayırmak
word_tokens = nltk.word_tokenize(text)
print(word_tokens)


#%%  cumle tokenizasyonu

sentence_tokens= nltk.sent_tokenize(text)
print(sentence_tokens)