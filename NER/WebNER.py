# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:55:53 2020

@author: Sushom-Dell
"""

import spacy
from spacy import displacy
from collections import Counter
from spacy.lang.en import English
import en_core_web_sm

#import webbrowser
nlp = en_core_web_sm.load()

doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
tags = [(X.text, X.label_) for X in doc.ents]

from flask import Flask, jsonify, request,render_template,redirect, url_for
app = Flask(__name__)
app.config["DEBUG"] = True
 
@app.route("/")
def index():
    return "<h1>To find NER, append /ner/</h1>"
 
@app.route("/ner/")
def NER():
    return render_template("ananya.html")

@app.route("/getNER/", methods=['POST','GET'])
def form():
    
    if(str(request.form["url_ip"])):
        tags = getNerTagsFromURl(str(request.form["url_ip"]))
    elif(str(request.form["txt_ip"])):
        tags = getNerTags(str(request.form["txt_ip"]))
    
    #return tags
    return render_template("ananya.html", tags=tags)

def getNerTagsFromURl(url):
    #retrieve article from url
    #get ner tags
    print(url)
    return 1

def getNerTags(inputText): 
    print("text:", inputText)
    doc1 = nlp(inputText)
    sentences = [x.text for x in doc1.sents]
    X = displacy.render(nlp(str(sentences)), jupyter=None, style='ent')
    return X
app.run()