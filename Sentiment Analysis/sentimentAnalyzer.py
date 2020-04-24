# -*- coding: utf-8 -*-

import requests, nltk, re, json, os, string
from flask import Flask, render_template, request, flash, url_for, jsonify
import sys, warnings, itertools
warnings.filterwarnings("ignore")
from sklearn.externals import joblib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import pickle as pkl
from textblob import TextBlob
from enchant.checker import SpellChecker
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


app = Flask(__name__)
 
@app.route("/")
 
@app.route("/Sentiment Analysis/")
def sentimentAnalysis():
    return render_template("sentimentAnalysisHome.html")

@app.route("/getSentiment/", methods=['POST','GET'])
def generate():
	paragraphInput = request.get_json(force=True)
	text = paragraphInput['text']
	iD = paragraphInput['id']
	#text = request.form['txt_ip']
	#iD = request.form['id']
	print(text,iD)
	generatedSentiment = getSentimentLabel(text, int(iD))
	print(generatedSentiment)
	return jsonify(generatedSentiment)

def loadPicklesItems():
	acronyms = joblib.load('Pickles/contractionMapping.pkl')
	tfidfFeatureVector = joblib.load('Pickles/tfidfFeatureVector.pkl')
	mlpCodeMixedModel = joblib.load('Pickles/mlpCodeMixedModel.pkl') 
	listAcronyms = list(acronyms)
	return listAcronyms, acronyms, tfidfFeatureVector, mlpCodeMixedModel

def dataPreprocess(data):
    preprocessedSentence = []
    for sentence in data:
        newTokens = []
        removetable = str.maketrans('', '', string.punctuation)
        removetable1 = str.maketrans('', '', string.digits)
        wordsOfSentence = sentence.split()
        for word in wordsOfSentence:
            word = word.lower()
            word = word.translate(removetable)
            word = word.translate(removetable1)
            if(len(word)>1 and word.startswith('@')!=True and word.startswith('<')!=True and word.startswith('www')!=True and word.startswith('http')!=True and word.endswith('com')!=True):
                word = re.sub(r'(.)\1+', r'\1\1', word)
                newTokens.append(word)
        if(len(newTokens)==0):
            wordsOfSentence = [x.lower() for x in wordsOfSentence]
            preprocessedSentence.append(wordsOfSentence)
        else:
            preprocessedSentence.append(newTokens)
    return preprocessedSentence

def findInputLanguage(text):
	maxErrorCount = 3
	englishWordsDictionary = SpellChecker("en_US")
	englishWordsDictionary.set_text(text)
	errors = [err.word for err in englishWordsDictionary]
	print(len(text.split()))
	if ((len(errors) > maxErrorCount)):
		return("Input text is not English!")
	else:
		return("None")

def findTextblobLabel(text):
	textObject = TextBlob(text)
	score = textObject.sentiment.polarity
	label = "Neutral"
	if(-0.25<=score<=0.25):
		label ="Neutral"
	elif(-0.25>score):
		label = "Negative"
	elif(0.25<score):
		label = "Positive"
	return label

def findVaderLabel(text):
	vaderObject = SentimentIntensityAnalyzer()
	score = vaderObject.polarity_scores(text)
	score = dict(itertools.islice(score.items(), 3))
	label = max(score.keys(), key=(lambda k: score[k]))
	if(label=='neg'):
		label='Negative'
	elif(label=='pos'):
		label='Positive'
	else:
		label='Neutral'
	return label

def getSentimentLabel(markedText,SystemID):
	sentimentLabelDictionary={}
	if(len(markedText.strip())==0):
		sentimentLabelDictionary['label']='None'
		sentimentLabelDictionary['error']='Please enter valid input!'
	else:
		listAcronyms, acronyms, tfidfFeatureVector, mlpCodeMixedModel = loadPicklesItems()
		preprocessedWords = dataPreprocess([markedText])
		preprocessedSentence = [' '.join(i) for i in preprocessedWords]
		if SystemID==100:
			error = findInputLanguage(preprocessedSentence[0])
			textblobLabel =findTextblobLabel(preprocessedSentence[0])
			vaderLabel = findVaderLabel(preprocessedSentence[0])
			outputLabel=max([textblobLabel, vaderLabel])
			if(error!='None'):
				outputLabel='None'
		elif  SystemID == 101:
			error = 'None'
			inputTfidfVector = tfidfFeatureVector.transform(preprocessedSentence).toarray()
			predictedLabel = mlpCodeMixedModel.predict(inputTfidfVector)
			outputLabel =predictedLabel[0]
		sentimentLabelDictionary['label'] = outputLabel		
		sentimentLabelDictionary['error']=error
	return sentimentLabelDictionary
	
app.run(host='0.0.0.0', port = 5000, debug=True)
