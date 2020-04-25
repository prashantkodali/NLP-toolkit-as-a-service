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

    def __init__(self,inpTyp,input):
        self.inpTyp = inpTyp
        self.input  = str(input)

    def isNotEnglish(self):
        input = self.input
        try:
            input.encode('ascii')
        except UnicodeEncodeError:
            input.encode('utf-8')
            return True
        else:
            return False
        

    def isEmpty(self):
        if(not (self.input and self.input.strip())): 
            return True
        else:
            return None		

    def validateInput(self):
        if(self.isEmpty()):
            return "Please provide input."
        elif(self.isNotEnglish()):
            return "Please provide input in English."
        else:
            return True
			
        