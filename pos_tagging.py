# -*- coding: utf-8 -*-
"""pos_tagging.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15adVjEuehIUrj4ofYxpz0bSeR_3JGZ-Q

assingning grammatical categories
"""

import nltk
try:
    nltk.data.find('taggers/averaged_perceptron_tagger_eng')
except LookupError:
    nltk.download('averaged_perceptron_tagger_eng')

text="the quick brown fox jumps over the lazy dog"
words=word_tokenize(text)
pos_tags=nltk.pos_tag(words)
print(pos_tags)