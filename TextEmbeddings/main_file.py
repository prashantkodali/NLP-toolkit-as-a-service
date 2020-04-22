# -*- coding: utf-8 -*-

import requests
import re
from spacy import displacy
from flask import Flask, render_template, request, flash, url_for, jsonify
from TextEmbeddings import *

import json

app = Flask(__name__)
#app.config["DEBUG"] = True
 
@app.route("/")
 
#@app.route("/TextEmbeddings")
#def TextEmbeddings():
#	return render_template("textembeddings.html")

@app.route("/GenerateEmbeddings", methods=['POST','GET'])

#def generate():
def GenerateEmbeddings():
	paragraphInput = request.get_json(force=True)
	text = paragraphInput['text']
	iD = paragraphInput['id']
	#text=str(request.form['txt_ip'])
	#iD = int(request.form['id'])
	print(text,iD)
	s = EmbeddingGenerator(text)
	GeneratedEmbedding = s.getEmbeddings(text, int(iD))
	#print(GeneratedEmbedding)
	return jsonify(GeneratedEmbedding)
 

app.run(host='0.0.0.0', port = 5000, debug=True)
