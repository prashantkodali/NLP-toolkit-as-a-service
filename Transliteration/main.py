'''
Runs a flask service for exposing the APIs.
'''


from flask import Flask, render_template, request, flash, url_for, jsonify
from isotrans import isotrans
from errorCheck import *


def errorDetect(text):
    print("in errorDetect")
    ec = errorCheck(text)
    print(ec.CheckInput())
    return ec.CheckInput()

app = Flask(__name__)


@app.route('/transliterate', methods=['POST'])
def transliterate():

    req_data = request.get_json()
    text = req_data['text']

    errorStatus = errorDetect(text)

    print(errorStatus)

    if errorStatus == False:
        transliterator = isotrans()
        transliterated_text = transliterator.transliterate(text)
        td = {'transliterated_text' : transliterated_text,'error':'None'}
        return jsonify(td)
    else:
        return jsonify({'transliterated_text':'None','error':errorStatus})


if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 7000, debug=True)
