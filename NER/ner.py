# -*- coding: utf-8 -*-
"""
******************************************************************************************************************
@author: Ananya Mukherjee
Name: ner.py
Description : This program retrieves the named entity tags using SpaCy's Model trained on OntoNotes5.

Input : Input Type and Input Text. 
If the input provided is URL then extracts the webpage by webscrapping and further Named Entity Recognition is applied.
If the input is in text form then Named Entity Recognition is applied on the sentences.
Output : Returns the NER tagged annotated text marked by HTML (for display purpose in client's browser) and Plain Annotated Text.

******************************************************************************************************************
"""
from bs4 import BeautifulSoup
import requests
import re

from spacy import displacy
import en_core_web_sm

nlp = en_core_web_sm.load()

class RetrieveNER:

    def __init__(self,inpTyp,input):
        self.inpTyp = inpTyp
        self.input  = str(input)

    def renderNerOutput(self,text):
        return displacy.render(text, jupyter=None, style='ent')

    def getAnnotatedOutput(self,document):
        return [(X, X.ent_type_) for X in document]

    def url_to_string(self,url):
        res = requests.get(url)
        html = res.text
        soup = BeautifulSoup(html, 'html5lib')
        for script in soup(["script", "style", 'aside']):
            script.extract()
        return " ".join(re.split(r'[\n\t]+', soup.get_text()))
	
    def getNerTagsFromURl(self,url):
        ny_bb = self.url_to_string(url) 
        return (self.renderNerOutput(nlp(ny_bb)),self.getAnnotatedOutput(nlp(ny_bb)))


    def getNerTagsFromText(self,inputText): 
        document = nlp(inputText)
        sentences = [x.text for x in document.sents]
        sentences = nlp(str(" ".join(sentences)))
		
        return (self.renderNerOutput(sentences),self.getAnnotatedOutput(document))

	

    def RetrieveNER(self):
        if(self.inpTyp == 'url'):		
            htmltags,tags = self.getNerTagsFromURl(self.input)
        
        elif(self.inpTyp == 'text'):	
            htmltags,tags = self.getNerTagsFromText(self.input)
	
        return htmltags,str(tags)