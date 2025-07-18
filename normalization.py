# -*- coding: utf-8 -*-
"""normalization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GID4dQixahXCt7rnpwc8w4ORVgPknsGs
"""

text = "There  were once Three Little Pigs! They lived in  a straw hut, a stick hut, and a brick hut."

# Lower case
normalized_text = text.lower()

# Remove punctuation
normalized_text = "".join([char for char in normalized_text if char.isalnum() or char.isspace()])

# Remove extra spaces
normalized_text = " ".join(normalized_text.split())

print("Original Text:", text)
print("Normalized Text:", normalized_text)