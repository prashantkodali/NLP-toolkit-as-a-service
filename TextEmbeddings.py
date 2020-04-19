# -*- coding: utf-8 -*-


from collections import Counter
from bs4 import BeautifulSoup
import requests
import re

from spacy import displacy
import en_core_web_sm
from flask import Flask, render_template, request, flash, url_for, jsonify
import transformers
import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel
import json

app = Flask(__name__)
#app.config["DEBUG"] = True
 
@app.route("/")
 
@app.route("/TextEmbeddings/")
def TextEmbeddings():
    return render_template("textembeddings.html")

@app.route("/getEmbeddings/", methods=['POST','GET'])

def form():
	req_data = request.get_json() #req_data is a dict. 
	text = req_data['text']
	Sentence_Embeddings_Dict = getEmbeddings(text)
	return jsonify(Sentence_Embeddings_Dict)

def SentenceVector(encoded_layers):
	token_vecs = encoded_layers[11][0]
	sentence_embedding = torch.mean(token_vecs, dim=0)
	return(sentence_embedding)

def getEmbeddings(marked_text): 
	Sentence_Embeddings_Dict={}
	model = BertModel.from_pretrained('bert-base-uncased')
	tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
	model.eval()
	marked_text = "[CLS] " + text + " [SEP]"
	tokenized_text = tokenizer.tokenize(marked_text)
	indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
	segments_ids = [1] * len(tokenized_text)
	tokens_tensor = torch.tensor([indexed_tokens])
	segments_tensors = torch.tensor([segments_ids])
	with torch.no_grad():
		encoded_layers, _ = model(tokens_tensor, segments_tensors)
	sentence_vec = SentenceVector(encoded_layers)
	Sentence_Embeddings_Dict['Embedding']=sentence_vec.tolist()
	#print ("Our final sentence embedding vector of shape:", sentence_vec.size())
	return Sentence_Embeddings_Dict
	
app.run(host='0.0.0.0', port = 5000, debug=True)
