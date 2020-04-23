from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from onmt.translate import TranslationServer, ServerModelError
from flask import jsonify
from sacremoses import MosesPunctNormalizer
mpn = MosesPunctNormalizer()

class basicTokenizer(object):
	"""
	Class for basic tokenizer which either uses nltk sentence and word tokenizer or user defined tokenizer. Main function of this class is wordTokenizer and sentTokenizer, which as name suggest takes in text to normalize and then tokenize. isEnglish is check function to confirm if input doesn't have any non English characters. 

	input: paragraph of text 
	output: text which is word and sentence tokenized
	"""
	def __init__(self, pathToWordTokModule, pathToSentTokModule):

		self.pathToWordTokModule = pathToWordTokModule
		self.pathToSentTokModule = pathToSentTokModule
		
	def wordTokenizer(self,paragraphTokenizedInput):

		if self.pathToWordTokModule =='wordNltk':
			listOfTokenizedSentences = [mpn.normalize(" ".join(word_tokenize(sentence))) for sentence in paragraphTokenizedInput]
		else:
			# can extend tokenizer with another tokenizer class for 
			listOfTokenizedSentences = [" ".join(self.pathToWordTokModule.wordTokenizer(sentence)) for sentence in paragraphTokenizedInput]

		return listOfTokenizedSentences

	def isEnglish(self,sentence):
		try:
			sentence.encode('ascii')
		except UnicodeEncodeError:
			sentence.encode('utf-8')
			return False
		else:
			return True

	def checkForErrors(self,listOfTokenizedSentences):
		for sentence in listOfTokenizedSentences:
			if self.isEnglish(sentence) == False:
				return "Non English Characters, Kindly Check"
		return "None"

	def sentTokenizer(self,paragraphInput):
		if self.pathToSentTokModule =='sentNltk':
			tokenizeParaIntoSentences = sent_tokenize(paragraphInput)
		else:
			# can extend tokenizer with another tokenizer class for 
			tokenizeParaIntoSentences = self.pathToSentTokModule.sentTokenizer(paragraphInput)
		return tokenizeParaIntoSentences
	

class translationPipeline(object):
	"""
	This class represents basic translation pipeline - preprocessing, translation and return the translation. Functionality of methods is self-explainatory.
	"""
	def __init__(self,pathToWordTokModule, pathToSentTokModule, config):
		self.config = config
		self.tokenizer = basicTokenizer(pathToWordTokModule, pathToSentTokModule)
		self.translationServer = TranslationServer()
		self.translationServer.start(self.config)

	
	def preprocessingInput(self, inputText):
		print ('input Sentence ',inputText)
		paragraphToTokenizedSent = self.tokenizer.sentTokenizer(inputText[0]['src'])
		print('Sentence tokenization of input: ',paragraphToTokenizedSent)
		listOfTokenizedSentences = self.tokenizer.wordTokenizer(paragraphToTokenizedSent)
		print('Word Tokenization of sentence segmented input: ',listOfTokenizedSentences)
		mtSystemID = int(inputText[0]['id'])
		listOfTokenizedSentences = self.specialPreprocessingForModels(listOfTokenizedSentences, mtSystemID)
		inputError = self.tokenizer.checkForErrors(listOfTokenizedSentences)
		return listOfTokenizedSentences, mtSystemID, inputError

	def specialPreprocessingForModels(self,listOfTokenizedSentences, modelID):
		"""
		There are models which uses slightly different preprocessing steps when dealing with text. These unique preprocessing steps for respective models can be included here.
		"""
		if modelID == 100:
			listOfTokenizedSentences = [sentence.lower() for sentence in listOfTokenizedSentences]
		else:
			listOfTokenizedSentences = listOfTokenizedSentences
		return listOfTokenizedSentences
		
	def translate(self,listOfTokenizedSentences, mtSystemID):
		inputToserver = [{'id':mtSystemID}]
		outputFromServer={}
		print ('after every tokenization: ',listOfTokenizedSentences)
		for sentence in listOfTokenizedSentences:
			inputToserver[0]['src']=sentence
			output = {}
			try:
				  translation, scores, n_best, times = self.translationServer.run(inputToserver)
				  assert len(translation) == len(inputToserver)
				  assert len(scores) == len(inputToserver)
				  output = [{"src": inputToserver[i]['src'], "tgt": translation[i],
						"n_best": n_best,
						"pred_score": scores[i]}
						for i in range(len(translation))]
			except ServerModelError as e:
				  output['error'] = str(e)
				  output['status'] = STATUS_ERROR
			if 'src' not in outputFromServer:
				  outputFromServer['src']=[output[0]['src']]
				  outputFromServer['tgt']=[output[0]['tgt']]
			else:
				  outputFromServer['src'].append(output[0]['src'])
				  outputFromServer['tgt'].append(output[0]['tgt'])
		outputFromServer['src']="\n\n".join(outputFromServer['src'])
		outputFromServer['tgt']="\n\n".join(outputFromServer['tgt'])
		print ('Translation Output:', outputFromServer['tgt'])
			
		return outputFromServer
