# -*- coding: utf-8 -*-
"""
******************************************************************************************************************
@author: Ananya Mukherjee
Name: ner.py
Description : This program preprocess the input and checks validation.

Input : Input Type and Input Text. 
Checks if entered input is empty or not.
Checks if entered input is in English or not.

Output : Returns 'Error Message' if an error is encountered else returns 'True'.

******************************************************************************************************************

"""
class PreProcess:

    def __init__(self,hyp,ref):
        self.hyp = hyp
        self.ref = ref

    def matchSentenceCount(self,hyplist,reflist):
        if(len(hyplist) == len(reflist)): 
            print(len(hyplist),len(reflist))
            return None
        else:
            return True	    

    def isEmpty(self):
        if(not (self.hyp.strip() and self.ref.strip())): 
            return True
        else:
            return None		

    def sentenceTokenize(self):
        return self.ref.split(u"\n"), self.hyp.split(u"\n")
		
    def validateInput(self):
        reflist, hyplist = self.sentenceTokenize()
        if(self.isEmpty()):
            return "Please provide both hypothesis and reference sentences.",[],[]    
        elif(self.matchSentenceCount(hyplist,reflist)):
            return "Please provide equal no of hypothesis and reference sentences.",[],[]
        else:
            return True,hyplist,reflist
			
        