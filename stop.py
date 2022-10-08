import nltk
from nltk.tokenize import word_tokenize as wt
from nltk.corpus import stopwords as sw
text=''' The ABCD lesson. The apple was placed in a ball and the cat was playing with it.
The dog hated the cat but loved the ball, he did not care for the apple. An apple is different from the apple, a apple is wrong.
'''
text = text.lower()
stops = sw.words('english')
tokens=wt(text)
print("Before removal\n")
print(tokens)
for token in tokens:
    if token in stops:
        tokens.remove(token)
print("\nAfter removal\n")
print(tokens)