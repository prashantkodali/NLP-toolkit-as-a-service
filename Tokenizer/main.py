from bs4 import BeautifulSoup
from json2html import json2html
from flask import Flask, jsonify, request,render_template,redirect, url_for
import requests
from tokenizers import ByteLevelBPETokenizer, SentencePieceBPETokenizer, BertWordPieceTokenizer
import re
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from validate import *
nltk.download('punkt')

# Bert vocabularies
bertBaseCased = "bert-base-cased-vocab.txt"
bertBaseUncased = "bert-base-uncased-vocab.txt"
bertLargeCased = "bert-large-cased-vocab.txt"
bertLargeUncased = "bert-large-uncased-vocab.txt"
# GPT-2 vocabularies
gpt2Vocab = "gpt2-vocab.json"
gpt2LargeVocab = "gpt2-large-vocab.json"

"""
    Starting flask API server for mtSystem.
    input: [{"input_text": "Input sentence here"]
        input_text : sentences that needs to be tokenized
    output: {"output_text": "normalized and tokenized input sentence" 
             }
"""

def validInput(text):
    p = PreProcess(text)
    return p.validateInput()

app = Flask(__name__)
#app.config["DEBUG"] = True 

@app.route("/")
def index():
    return "<h1>To find Tokenization, append /tokenizer/</h1>"

@app.route("/tokenizer")
def tokens():
    return render_template("tokens.html")

@app.route("/gettokenizer", methods=['POST'])
def form():
    inputjson = request.get_json()
    input_text = inputjson['input_text']
    check = validInput(input_text)
    if(check==True):    
        value = int(inputjson['id'])
        if(value==100):
            tokens = HuggingFaceTokenizer(str(input_text))
        elif(value==201):
            tokens = SentTextTokenizer(str(input_text))
        elif(value==101):
            tokens = nltktokenizer(str(input_text))
        print(tokens)
        return jsonify({'output_text':tokens,'error':None})
    else:
        return jsonify({'output_text':None,'error':check})

def HuggingFaceTokenizer(inputText): 
    sentence = inputText
    WordPiece = BertWordPieceTokenizer(bertLargeUncased)
    WordPieceEncoder = WordPiece.encode(sentence)
    return WordPieceEncoder.tokens

def SentTextTokenizer(inputText): 
    sentence = inputText
    tokens = sent_tokenize(sentence)
    return tokens

def nltktokenizer(inputText):
    tokens = word_tokenize(inputText)
    print(tokens)
    return tokens

app.run(host='0.0.0.0', port = 8080, debug=True)