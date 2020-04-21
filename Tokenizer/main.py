from collections import Counter
from bs4 import BeautifulSoup
import requests
import re
from json2html import json2html
from spacy import displacy
import en_core_web_sm
from flask import Flask, jsonify, request,render_template,redirect, url_for
import requests
from tokenizers import ByteLevelBPETokenizer, SentencePieceBPETokenizer, BertWordPieceTokenizer

nlp = en_core_web_sm.load()
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
    input = inputjson['input_text']
    # input = JsonInput["txt_ip"]
    # input= request.form["txt_ip"]
    print(input)
    tokens= gettokens(str(input))
    print(tokens)
    return jsonify({'output_text':tokens})

def gettokens(inputText): 
    # Instantiate a Bert tokenizers
    sentence = inputText
    WordPiece = BertWordPieceTokenizer(bertLargeUncased)
    WordPieceEncoder = WordPiece.encode(sentence)
    # Print the ids, tokens and offsets
    # print(WordPieceEncoder.ids)
    # print(WordPieceEncoder.tokens)
    # print(WordPieceEncoder.offsets)
    # X = displacy.render(WordPieceEncoder.tokens, jupyter=None, style='ent')
    return WordPieceEncoder.tokens

# Bert vocabularies
bertBaseCased = "bert-base-cased-vocab.txt"
bertBaseUncased = "bert-base-uncased-vocab.txt"
bertLargeCased = "bert-large-cased-vocab.txt"
bertLargeUncased = "bert-large-uncased-vocab.txt"
# GPT-2 vocabularies
gpt2Vocab = "gpt2-vocab.json"
gpt2LargeVocab = "gpt2-large-vocab.json"

app.run(host='0.0.0.0', port = 8080, debug=True)