import transformers
import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel
from transformers import AlbertModel, AlbertTokenizer
from transformers import DistilBertModel,DistilBertTokenizer
import numpy as np

class EmbeddingGenerator:

	def __init__(self,marked_text):
		self.marked_text = marked_text
        

	def SentenceVector(self,encoded_layers):
		token_vecs = encoded_layers[11][0]
		sentence_embedding = torch.mean(token_vecs, dim=0)
		return(sentence_embedding)


	def IndexOfTokens(self,tokenizer):
		tokenized_text = tokenizer.tokenize(self.marked_text)
		indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
		segments_ids = [1] * len(tokenized_text)
		return(torch.tensor([indexed_tokens]),torch.tensor([segments_ids]))

	def getBertEmbeddings(self):
		model = BertModel.from_pretrained('bert-base-uncased')
		tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
		model.eval()
		tokens_tensor, segments_tensors = self.IndexOfTokens(tokenizer)
		with torch.no_grad():
			encoded_layers, _ = model(tokens_tensor, segments_tensors)
		sentence_vec = self.SentenceVector(encoded_layers)
		#print("--",sentence_vec.tolist())
		return(sentence_vec.tolist())

	def getDistilBertEmbeddings(self):
		model = DistilBertModel.from_pretrained('distilbert-base-uncased')
		tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
		model.eval()
		tokens_tensor, segments_tensors = self.IndexOfTokens(tokenizer)
		with torch.no_grad():
			last_hidden_states = model(tokens_tensor, attention_mask=segments_tensors)
		features = last_hidden_states[0][:,0,:].numpy()
		features = np.reshape(features,features.shape[1])
		return(features.tolist())

	def getAlBertEmbeddings(self):
		model = AlbertModel.from_pretrained('albert-base-v2')
		tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
		model.eval()
		tokens_tensor, segments_tensors = self.IndexOfTokens(tokenizer,marked_text)
		with torch.no_grad():
			last_hidden_states = model(tokens_tensor, attention_mask=segments_tensors)
		features = last_hidden_states[0][:,0,:].numpy()
		features = np.reshape(features,features.shape[1])

	def getEmbeddings(self,marked_text,SystemID):
		Sentence_Embeddings_Dict={}
		self.marked_text = "[CLS] " + marked_text + " [SEP]"
		if SystemID==100:
			Sentence_Embeddings_Dict['embeddings']= self.getBertEmbeddings()
		elif  SystemID == 101:
			Sentence_Embeddings_Dict['embeddings']= self.getDistilBertEmbeddings()
		elif SystemID == 102:
			Sentence_Embeddings_Dict['embeddings']= self.getAlBertEmbeddings()
		return Sentence_Embeddings_Dict
