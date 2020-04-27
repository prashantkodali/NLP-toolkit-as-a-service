class errorCheck:

    def __init__(self,input):
        self.input  = str(input)

    def isNotEnglish(self):
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
        elif(self.isNotEnglish()):
            return "Please do not provide input in English."
        else:
            return False
