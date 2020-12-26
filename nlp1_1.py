#!/usr/bin/env python
# coding: utf-8

# In[1]:


from konlpy.tag import Kkma
from collections import Counter

infile = open("소나기.txt", encoding='utf-8')
data=infile.read()

kkma = Kkma()
words=kkma.morphs(data)

vocab=Counter(words)
vocab = dict((k, v) for k, v in vocab.items() if v >= 5)
print(vocab)


# In[ ]:




