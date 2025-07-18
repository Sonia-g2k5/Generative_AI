# -*- coding: utf-8 -*-
"""nlp_models.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zPv6BSmG6WJW4nlPOInAbwa9aC_cGg3c
"""

# Install Transformers
!pip install transformers -q

from transformers import pipeline

# Load Hugging Face Pipelines
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
ner_tagger = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)
translator = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")

def nlp_assistant(sentence):
    # Sentiment Analysis
    sentiment_result = sentiment_analyzer(sentence)[0]
    sentiment = f"{sentiment_result['label']} (Score: {sentiment_result['score']:.2f})"

    # Named Entity Recognition
    ner_result = ner_tagger(sentence)
    named_entities = [f"{ent['word']} ({ent['entity_group']})" for ent in ner_result]
    if not named_entities:
        named_entities = ["No named entities found."]

    # Translation to German
    translated = translator(sentence)[0]['translation_text']

    # Print Output
    print("\n📌 Input Sentence:")
    print(sentence)
    print("\n🧠 Sentiment Analysis:")
    print(sentiment)
    print("\n🔍 Named Entities:")
    for entity in named_entities:
        print(f" - {entity}")
    print("\n🌍 German Translation:")
    print(translated)

# Example Usage
if __name__ == "__main__":
    print("🧠 Hugging Face NLP Assistant")
    user_input = input("Enter a sentence: ")
    nlp_assistant(user_input)