# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:55:53 2020

@author: Sushom-Dell
"""
from collections import Counter
from bs4 import BeautifulSoup
import requests
import re

from spacy import displacy
import en_core_web_sm
from flask import Flask, jsonify, request,render_template,redirect, url_for


nlp = en_core_web_sm.load()

app = Flask(__name__)
#app.config["DEBUG"] = True
 
@app.route("/")
def index():
    return "<h1>To find NER, append /ner/</h1>"
 
@app.route("/ner/")
def NER():
    return render_template("ner.html")

@app.route("/getNER/", methods=['POST','GET'])
def form():
    
    if(str(request.form["url_ip"])):
        tags = getNerTagsFromURl(str(request.form["url_ip"]))
        
    elif(str(request.form["txt_ip"])):
        tags = getNerTags(str(request.form["txt_ip"]))
    
    return render_template("ner.html", tags=tags)

def getNerTagsFromURl(url):
    #retrieve article from url
    ny_bb = url_to_string(url)
    
    article = nlp(ny_bb)
    labels = [x.label_ for x in article.ents]
    cnt_dict = Counter(labels) #print the cardinality 
    
    X = displacy.render(article, jupyter=None, style='ent')
    print(len(article.ents))
   #sentences = [x for x in article.sents]
   # print(str(sentences[20]))
    #get ner tags
    print(url)
    return X

def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))

def getNerTags(inputText): 
    #print("text:", inputText)
    doc1 = nlp(inputText)
    sentences = [x.text for x in doc1.sents]
    X = displacy.render(nlp(str(sentences)), jupyter=None, style='ent')
    return X
	
app.run(host='0.0.0.0', port = 5000, debug=True)
