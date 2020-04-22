# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:55:53 2020
@author: Ananya Mukherjee
#***********************************************************************************************
#Description : Server Side Program
#Model : SpaCy’s named entity recognition model is trained on OntoNotes5 corpus. 
#      : Assigns context-specific token vectors, POS tags, dependency parse and named entities.
#***********************************************************************************************
"""
from collections import Counter
from bs4 import BeautifulSoup
import requests
import re
from json2html import json2html
from spacy import displacy
import en_core_web_sm
from flask import Flask, jsonify, request,render_template,redirect, url_for
import requests

#Loads the model trained on CNN 
nlp = en_core_web_sm.load()

app = Flask(__name__)

@app.route("/getNER", methods=['POST','GET'])
def form():
    JsonInput = request.get_json(force=True)
    inpTyp = JsonInput['type']
    input = JsonInput['text']
    print(inpTyp,input)
    if(inpTyp == 'url'):
        tags = getNerTagsFromURl(str(input))
        
    elif(inpTyp == 'text'):
        tags = getNerTags(str(input))

    return jsonify({'output_text':tags})

def getNerTagsFromURl(url):
    ny_bb = url_to_string(url)
    
    article = nlp(ny_bb)
    labels = [x.label_ for x in article.ents]
    cnt_dict = Counter(labels) #print the cardinality 
    
    X = displacy.render(article, jupyter=None, style='ent')
    print(len(article.ents))
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
    doc1 = nlp(inputText)
    sentences = [x.text for x in doc1.sents]
    X = displacy.render(nlp(str(sentences)), jupyter=None, style='ent')
    return X
	
app.run(host='0.0.0.0', port = 8080, debug=True)
