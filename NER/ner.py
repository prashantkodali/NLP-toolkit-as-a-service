from bs4 import BeautifulSoup
import requests
import re

from spacy import displacy
import en_core_web_sm
from flask import Flask, jsonify, request,render_template,redirect, url_for


nlp = en_core_web_sm.load()

class RetrieveNER:

    def __init__(self,inpTyp,input):
        self.inpTyp = inpTyp
        self.input  = str(input)

    def renderNerOutputFromText(self,text):
        return displacy.render(text, jupyter=None, style='ent')


    def url_to_string(self,url):
        res = requests.get(url)
        html = res.text
        soup = BeautifulSoup(html, 'html5lib')
        for script in soup(["script", "style", 'aside']):
            script.extract()
        return " ".join(re.split(r'[\n\t]+', soup.get_text()))
	
    def getNerTagsFromURl(self,url):
        ny_bb = url_to_string(url) 
        return self.renderNerOutputFromText(nlp(ny_bb))


    def getNerTagsFromText(self,inputText): 
        doc1 = nlp(inputText)
        sentences = [x.text for x in doc1.sents]
        sentences = " ".join(sentences)
        return self.renderNerOutputFromText(nlp(str(sentences)))
	

    def RetrieveNER(self):
        input = self.input
        if(self.inpTyp == 'url'):		
            tags = self.getNerTagsFromURl(input)
        
        elif(self.inpTyp == 'text'):	
            tags = self.getNerTagsFromText(input)
	
        return tags