# file to run the transformer (fine-tuning model)

import pandas as pd
import numpy as np
import sys
import os
import openai
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

#df = pd.read_csv('PoetryFoundationData.csv')
#print(df.iloc[2])

openai.api_key = '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'

TOKENIZER = None
MODEL = pipeline('text2text-generation', 'czearing/story-to-title')

with open('prompt.txt') as f:
    prompt = f.read()

def getTitle(poem):
    response = openai.Completion.create(
    engine="text-ada-001",
    prompt=prompt + poem + '\nTitle: ',
    temperature=0.7,
    max_tokens=750,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return response.choices[0].text

# With our "fine-tuned" model we now use pipelines for this...
def loadTransform():
    pass

def getTitle_1(poem):
    return MODEL(poem)[0]['generated_text']

