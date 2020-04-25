# -*- coding: utf-8 -*-
"""
******************************************************************************************************************
@author: Ananya Mukherjee
Name: mteval.py
Description : This program retrieves the BLEU Score and NIST Score

Input : hypothesis sentence, reference sentence 

Output : Returns BLEU Score and NIST Score

******************************************************************************************************************
"""

import nltk.translate.bleu_score as NB
import nltk.translate.nist_score as NN 
from nltk.translate.bleu_score import SmoothingFunction
sf = SmoothingFunction()

class MTEvaluation:

    def __init__(self,hyp,ref):
        self.hyp = hyp
        self.ref = ref

    def getNistScore(self,hypSent,refSent):
        return NN.sentence_nist([refSent.split()],hypSent.split(),n=5)

    def getBleuScore(self,hypSent,refSent): 
        return NB.sentence_bleu([refSent.split()],hypSent.split(), smoothing_function = sf.method7)

    def MTEvaluation(self):
        bScore = []
        nScore = []
        for i in range(len(self.ref)):  
            bScore.append(self.getBleuScore(self.ref[i],self.hyp[i]))
            nScore.append(self.getNistScore(self.ref[i],self.hyp[i]))
        return bScore,nScore