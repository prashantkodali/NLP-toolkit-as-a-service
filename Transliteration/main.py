'''
Runs a flask service for exposing the APIs.

Exposes one api :/transliterate to get this up and working.

Return output json, after processing the input which in recieved as a json.

Does error detection, for wrong inputs, using the error cases implemented in the errorCheck.py
'''


from flask import Flask, render_template, request, flash, url_for, jsonify
from isotrans import isotrans
from errorCheck import *


def errorDetect(text):
    ec = errorCheck(text)
    return ec.CheckInput()

app = Flask(__name__)

@app.route('/transliterate', methods=['POST'])
def transliterate():

    req_data = request.get_json()
    text = req_data['text']

    errorStatus = errorDetect(text)#errorStatus is True is one of the validation cases fails, False otherwise.

    if errorStatus == False:
        transliterator = isotrans()
        transliterated_text = transliterator.transliterate(text)
        td = {'transliterated_text' : transliterated_text,'error':'None'}
        return jsonify(td)
    else:
        return jsonify({'transliterated_text':'None','error':errorStatus})


if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 7000, debug=True)#can be changed by user if this to be run on another port.
