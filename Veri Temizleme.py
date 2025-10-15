#veri temizleme 
#metinlerdeki fazla bosluklari temizleme ornek

text = "Hello,      World!      2035"
text.split()
cleaned_text1 =" ".join(text.split())

print(cleaned_text1)

#buyukten kucuge harf cevırmek

text="Hello, World! 2035"
cleaned_text2 = text.lower()
print(cleaned_text2)

#noktalama isaretlerini kaldir

import string

text="Hello, World! 2035"
cleaned_text3 = text.translate(str.maketrans("", "" , string.punctuation))
print(cleaned_text3)

#ozel karakterleri kaldir

import re

text="Hello, World! 2035"
cleaned_text4 = re.sub(r"[^A-Za-z0-9\s]","", text)
print(cleaned_text4)

#yazim hatalarını düzelt

from textblob import TextBlob

text="Helıo, Wirld! 2035"
Cleaned_text5 = str(TextBlob(text).correct())
print(Cleaned_text5)


#html ya da url etitkerlerini kaldırma

from bs4 import BeautifulSoup

html_text = "<div>Hello, World! 2035</div>"
Cleaned_text6 = BeautifulSoup(html_text, "html.parser").get_text()
print(Cleaned_text6)












