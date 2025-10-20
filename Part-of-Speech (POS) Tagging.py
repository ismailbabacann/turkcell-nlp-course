import spacy

nlp=spacy.load("en_core_web_sm")

sentence1 = "What is the weather like today?"
doc1 = nlp(sentence1)

for token in doc1:
        print(token.text, token.pos_)
        
        
sentence2 = "Artificial intelligence (AI) has rapidly evolved over the past decade, transforming industries and changing the way humans interact with technology. From virtual assistants like Siri and Alexa to advanced autonomous vehicles, AI has become an essential part of daily life. Many companies now rely on machine learning algorithms to analyze data, predict customer behavior, and improve decision-making processes. However, as AI systems become more complex, ethical concerns such as data privacy, algorithmic bias, and job displacement have gained increasing attention. Researchers are continuously working on developing transparent and fair AI models that not only perform efficiently but also ensure accountability. In the near future, AI is expected to play a major role in education, healthcare, and environmental sustainability, potentially reshaping the world in ways we can hardly imagine today."
doc2 = nlp(sentence2)

for token in doc2:
    print(token.text, token.pos_)