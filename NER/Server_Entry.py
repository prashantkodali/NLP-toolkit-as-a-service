# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:55:53 2020

@author: Sushom-Dell
"""


import requests
import re
from flask import Flask, jsonify, request,render_template,redirect, url_for
import requests
from ner import *
#from preprocess import *  (include code for checking english, throw error if text is empty, check for unicode)

app = Flask(__name__)

@app.route("/getNER", methods=['POST','GET'])
def getNamedEntities():
    JsonInput = request.get_json(force=True)
    inpTyp = JsonInput['type']
    input = JsonInput['text']
	
    ner_obj    = RetrieveNER(inpTyp,input)
    OutputTags = ner_obj.RetrieveNER()
    
    return jsonify({'output_text':OutputTags})


app.run(host='0.0.0.0', port = 8080, debug=True)