import transformers
import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel
from transformers import AlbertModel, AlbertTokenizer
from transformers import DistilBertModel,DistilBertTokenizer
import numpy as np
from enchant.checker import SpellChecker

class EmbeddingGenerator:

	def __init__(self,marked_text):
		self.marked_text = marked_text
	
	def is_in_english(self):
		max_error_count = 1
		d = SpellChecker("en_US")
		d.set_text(self.marked_text)
		errors = [err.word for err in d]
		if ((len(errors) >= max_error_count)):
			return("Input entered is not in English")
		else:
			return("None")

	def is_input_empty(self):
		if(not (self.marked_text and self.marked_text.strip())): 
			return "Input Entered is empty"
		else:
			return "None"

	def getInputValidated(self):
		result = self.is_input_empty()
		if result!="None" :
			return result
		result = self.is_in_english()
		if result!="None":
			return result
		if  result == "None":
			return "No_Error"
		
		
	def getSentenceVector(self,encoded_layers):
		token_vecs = encoded_layers[11][0]
		sentence_embedding = torch.mean(token_vecs, dim=0)
		return(sentence_embedding)


	def getIndexs(self,tokenizer):
		tokenized_text = tokenizer.tokenize(self.marked_text)
		indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
		segments_ids = [1] * len(tokenized_text)
		return(torch.tensor([indexed_tokens]),torch.tensor([segments_ids]))

	def getBertEmbeddings(self):
		model = BertModel.from_pretrained('bert-base-uncased')
		tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
		model.eval()
		tokens_tensor, segments_tensors = self.getIndexs(tokenizer)
		with torch.no_grad():
			encoded_layers, _ = model(tokens_tensor, segments_tensors)
		sentence_vec = self.getSentenceVector(encoded_layers)
		return(sentence_vec.tolist())

	def getDistilBertEmbeddings(self):
		model = DistilBertModel.from_pretrained('distilbert-base-uncased')
		tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
		model.eval()
		tokens_tensor, segments_tensors = self.getIndexs(tokenizer)
		with torch.no_grad():
			last_hidden_states = model(tokens_tensor, attention_mask=segments_tensors)
		features = last_hidden_states[0][:,0,:].numpy()
		features = np.reshape(features,features.shape[1])
		return(features.tolist())

	def getAlBertEmbeddings(self):
		model = AlbertModel.from_pretrained('albert-base-v2')
		tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
		model.eval()
		tokens_tensor, segments_tensors = self.getIndexs(tokenizer)
		with torch.no_grad():
			last_hidden_states = model(tokens_tensor, attention_mask=segments_tensors)
		features = last_hidden_states[0][:,0,:].numpy()
		features = np.reshape(features,features.shape[1])
		return(features.tolist())

	def getEmbeddings(self,marked_text,SystemID):
		Sentence_Embeddings_Dict={}
		self.marked_text = marked_text
		self.SystemID = SystemID
		errorReceived = self.getInputValidated()
		print("-----------",errorReceived)
		if(errorReceived!="No_Error"):
			Sentence_Embeddings_Dict['error'] = errorReceived
			Sentence_Embeddings_Dict['embeddings'] = "None"
			return(Sentence_Embeddings_Dict)
		self.marked_text = "[CLS] " + marked_text + " [SEP]"
		if SystemID==100:
			Sentence_Embeddings_Dict['embeddings']= self.getBertEmbeddings()
		elif  SystemID == 101:
			Sentence_Embeddings_Dict['embeddings']= self.getDistilBertEmbeddings()
		elif SystemID == 102:
			Sentence_Embeddings_Dict['embeddings']= self.getAlBertEmbeddings()
		Sentence_Embeddings_Dict['error'] = "None"
		return Sentence_Embeddings_Dict
