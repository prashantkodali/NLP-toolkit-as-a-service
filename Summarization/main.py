'''
Runs a flask service for exposing the APIs.

Uses classes detailed in summarizer.py for summarization methods.
'''


from flask import Flask, render_template, request, flash, url_for, jsonify
from summarizer import *


app = Flask(__name__)

word_vector_file = '/home/pk/Downloads/crawl-300d-2M.magnitude'

s = Summarizer(word_vector_file)

@app.route('/summarize', methods=['POST'])
def summarize():

    req_data = request.get_json()
    text = req_data['text']
    number_of_sentences = req_data['num']

    summarized_text = ".\n".join(s.summarize(text, number_of_sentences)) #stitching the returned sentences together.

    td = {'outputtext' : summarized_text} 

    return jsonify(td)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 6000, debug=True)
