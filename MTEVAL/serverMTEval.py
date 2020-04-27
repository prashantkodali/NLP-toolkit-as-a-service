# -*- coding: utf-8 -*-
"""
******************************************************************************************************************
@author: Ananya Mukherjee
Name: serverMTEval.py
Description : This program is the entry point of Automatic MT Evaluation Online Service Server. It accepts JSON input, preprocesses to validate and if no error then retrieves Translation Score.
Imports mteval and preprocessor.

Input : JSON Input from Client. (containing hypothesis and reference senentences)
Preprocess the input to check for errors.
If no errors, then retrieves Machine Translation Score (BLEU Score and NIST Score)
Output : Returns BLEU Score, NIST Score, Error Message (Error Message is None if no error is found.)

******************************************************************************************************************
"""


import requests
import re
from flask import Flask, jsonify, request,render_template,redirect, url_for
import requests

from mteval import *
from preprocessor import *

app = Flask(__name__)

	
@app.route("/getMTEval", methods=['POST','GET'])
def getMTEvaluation():
    JsonInput = request.get_json(force=True)
    hyp = JsonInput['hyp']
    ref = JsonInput['ref']
	
    msg,hyplist,reflist = processInput(hyp,ref)
    return output(hyplist,reflist,msg)

def processInput(hyp,ref):
    p = PreProcess(hyp,ref)	
    return p.validateInput()

def output(hyplist,reflist,msg):  
	if(msg == True):
		mteval_obj    = MTEvaluation(hyplist,reflist,)
		bScore, nScore = mteval_obj.MTEvaluation()
	
		return jsonify({'bleu':bScore,'nist':nScore,'error':None})		
	else:
		return jsonify({'bleu':None,'nist':None,'error':msg})

app.run(host='0.0.0.0', port = 8000, debug=True)
