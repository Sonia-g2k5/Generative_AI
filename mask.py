# -*- coding: utf-8 -*-
"""mask.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_OcovzvAnkxvFhbNfYFJDCq6XgtsiBeA
"""

from transformers import pipeline
unmasker = pipeline('fill-mask', model='bert-base-uncased')
unmasker("Hello I'm a [MASK] model.")