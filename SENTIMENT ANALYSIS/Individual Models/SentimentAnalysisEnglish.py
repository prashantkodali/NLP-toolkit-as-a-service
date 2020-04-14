import sys, warnings, itertools
warnings.filterwarnings("ignore")
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def commandLineText():
	length = len(sys.argv)
	text = ""
	for i in range(1, length): 
		text = text+" "+sys.argv[i] 
	text = text.strip()
	return text

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

inputText = commandLineText()
textblobLabel =findTextblobLabel(inputText)
vaderLabel = findVaderLabel(inputText)
print(max([textblobLabel, vaderLabel]))
