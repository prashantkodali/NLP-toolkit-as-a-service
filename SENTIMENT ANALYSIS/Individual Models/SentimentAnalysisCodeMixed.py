import sys, warnings, itertools
warnings.filterwarnings("ignore")
import nltk, re
from sklearn.externals import joblib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import pickle as pkl
import csv, os, string

def commandLineText():
	length = len(sys.argv)
	text = ""
	for i in range(1, length): 
		text = text+" "+sys.argv[i] 
	text = text.strip()
	return text

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

inputText = commandLineText()
listAcronyms, acronyms, tfidfFeatureVector, mlpCodeMixedModel = loadPicklesItems()
preprocessedWords = dataPreprocess([inputText])
preprocessedSentence = [' '.join(i) for i in preprocessedWords]
inputTfidfVector = tfidfFeatureVector.transform(preprocessedSentence).toarray()
predictedLabel = mlpCodeMixedModel.predict(inputTfidfVector)
print(predictedLabel[0])
