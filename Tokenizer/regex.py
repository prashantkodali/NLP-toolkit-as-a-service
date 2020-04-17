import re
text = raw_input("Enter your sentence here : ")
tokens = re.findall("[\w']+", text)
print(tokens)