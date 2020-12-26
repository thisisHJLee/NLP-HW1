#!/usr/bin/env python
# coding: utf-8

# In[1]:


from konlpy.tag import Kkma
from collections import Counter

infile = open("소나기.txt", encoding='utf-8')
data=infile.read()

kkma = Kkma()
words=kkma.morphs(data)

stop_list = ['을', '이', '가', '에', '를', '은', '의', '는', '도', '으로', '에서', '로', '나', '까지', '고', '라도', '부터', '에게', '마저', '에다']
result_list = []

vocab=Counter(words)

for k, v in vocab.items():
    if k not in stop_list:
        if v >= 5:
            result_list.insert(0, k)

print(result_list)

