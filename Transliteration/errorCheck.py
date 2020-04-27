'''
This class is implemented for basic input validation, to check if the input is
not as expected.
Currently implements two cases:
1. isEnglish: True if input is in english. Transliteration is from native script to roman and not other way round.
2. isEmpty: if no input is given. 
'''


class errorCheck:

    def __init__(self,input):
        self.input  = str(input)

    def isEnglish(self):
        input = self.input
        try:
            input.encode('ascii')
        except UnicodeEncodeError:
            input.encode('utf-8')
            return False
        else:
            return True


    def isEmpty(self):
        if(not (self.input and self.input.strip())):
            return True
        else:
            return None


    def CheckInput(self):
        if(self.isEmpty()):
            return "Please provide input."
        elif(self.isEnglish()):
            return "Please do not provide input in English."
        else:
            return False
