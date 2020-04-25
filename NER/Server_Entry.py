# -*- coding: utf-8 -*-
"""
@author: Ananya Mukherjee
Name :
Description : 

"""


import requests
import re
from flask import Flask, jsonify, request,render_template,redirect, url_for
import requests
from ner import *
from preprocessor import *

app = Flask(__name__)

	
@app.route("/getNER", methods=['POST','GET'])
def getNamedEntities():
    JsonInput = request.get_json(force=True)
    inpTyp = JsonInput['type']
    input = JsonInput['text']

    msg = processInput(inpTyp,input)
    return output(inpTyp,input,msg)

def processInput(inpTyp,input):
    p = PreProcess(inpTyp,input)	
    return p.validateInput()

def output(inpTyp,input,msg):  
	if(msg == True):
		ner_obj    = RetrieveNER(inpTyp,input)
		HTMLTags, AnnotatedTags = ner_obj.RetrieveNER()
		#print(AnnotatedTags)
		return jsonify({'output_text':HTMLTags,'annotated_tags':AnnotatedTags,'error':None})		
	else:
		return jsonify({'output_text':None,'annotated_tags':None,'error':msg})

app.run(host='0.0.0.0', port = 8080, debug=True)