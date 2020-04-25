'''
Runs a flask service for exposing the APIs.
'''


from flask import Flask, render_template, request, flash, url_for, jsonify
from indictrans import Transliterator

from isotrans import isotrans


app = Flask(__name__)


@app.route('/transliterate', methods=['POST'])
def summarize():

    req_data = request.get_json()
    text = req_data['text']


    transliterator = isotrans()
    transliterated_text = transliterator.transliterate(text)

    td = {'transliterated_text' : transliterated_text}
    return jsonify(td)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 7000, debug=True)
