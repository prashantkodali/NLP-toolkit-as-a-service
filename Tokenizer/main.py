from collections import Counter
from bs4 import BeautifulSoup
import requests
import re
from json2html import json2html
import en_core_web_sm
from flask import Flask, jsonify, request,render_template,redirect, url_for
import requests
from tokenizers import ByteLevelBPETokenizer, SentencePieceBPETokenizer, BertWordPieceTokenizer
import re
from nltk.tokenize import word_tokenize


# nlp = en_core_web_sm.load()
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
    print(inputjson)
    inputt = inputjson['txt_ip']
    value = int(inputjson['id'])
    tokens = 1
    if(value==100):
        tokens = HuggingFace(str(input))
    if(value==101):
        tokens = SplitText(str(input))
    if(value==102):
        tokens = nltkt(str(input))
    return jsonify({'output_text':tokens})

def HuggingFace(inputText): 
    sentence = inputText
    WordPiece = BertWordPieceTokenizer(bertLargeUncased)
    WordPieceEncoder = WordPiece.encode(sentence)
    return WordPieceEncoder.tokens

def SplitText(inputText): 
    sentence = inputText
    tokens = sentence.split()
    return tokens

def nltkt(inputText):
    tokens = word_tokenize(inputText)
    return tokens

# Bert vocabularies
bertBaseCased = "bert-base-cased-vocab.txt"
bertBaseUncased = "bert-base-uncased-vocab.txt"
bertLargeCased = "bert-large-cased-vocab.txt"
bertLargeUncased = "bert-large-uncased-vocab.txt"
# GPT-2 vocabularies
gpt2Vocab = "gpt2-vocab.json"
gpt2LargeVocab = "gpt2-large-vocab.json"

app.run(host='0.0.0.0', port = 8080, debug=True)