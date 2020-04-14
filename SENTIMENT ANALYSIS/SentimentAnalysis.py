import sys, warnings, itertools
warnings.filterwarnings("ignore")
import nltk, re
from sklearn.externals import joblib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import pickle as pkl
import csv, os, string
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def commandLineText():
	length = len(sys.argv)
	modelType = sys.argv[1]
	text = ""
	for i in range(2, length): 
		text = text+" "+sys.argv[i] 
	text = text.strip()
	return text, modelType

def loadPicklesItems():
	acronyms = joblib.load('Pickles/contractionMapping.pkl')
	tfidfFeatureVector = joblib.load('Pickles/tfidfFeatureVector.pkl')
	mlpCodeMixedModel = joblib.load('Pickles/mlpCodeMixedModel.pkl') 
	listAcronyms = list(acronyms)
	return listAcronyms, acronyms, tfidfFeatureVector, mlpCodeMixedModel

def findAcronyms(acronym):
    if(acronym in listAcronyms):
        return acronyms[acronym]
    else:
        return acronym

def dataPreprocess(data):
    preprocessedSentence = []
    for sentence in data:
        newTokens = []
        removetable = str.maketrans('', '', string.punctuation)
        removetable1 = str.maketrans('', '', string.digits)
        wordsOfSentence = sentence.split()
        for word in wordsOfSentence:
            word = word.lower()
            word = findAcronyms(word)
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

inputText, modelType = commandLineText()
listAcronyms, acronyms, tfidfFeatureVector, mlpCodeMixedModel = loadPicklesItems()
preprocessedWords = dataPreprocess([inputText])
preprocessedSentence = [' '.join(i) for i in preprocessedWords]
preprocessedWords = dataPreprocess([inputText])
preprocessedSentence = [' '.join(i) for i in preprocessedWords]
if(modelType=='1'):
	textblobLabel =findTextblobLabel(preprocessedSentence[0])
	vaderLabel = findVaderLabel(preprocessedSentence[0])
	print(max([textblobLabel, vaderLabel]))
elif(modelType=='2'):
	inputTfidfVector = tfidfFeatureVector.transform(preprocessedSentence).toarray()
	predictedLabel = mlpCodeMixedModel.predict(inputTfidfVector)
	print(predictedLabel[0])
else:
	print('Wrong Input Format')
	print('python3 --modelType --inputtext')
	print('modelType: 1-normalSentimentAnalysis, 2-codeMixedSentimentAnalysis')
