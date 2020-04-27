class errorCheck:

    def __init__(self,input):
        self.input  = str(input)

    def isEnglish(self):
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


    def CheckInput(self):
        print('in checkinput')
        if(self.isEmpty()):
            return "Please provide input."
        elif(self.isEnglish()):
            print(self.isEnglish())
            return "Please dont provide input in English."
        else:
            return False
