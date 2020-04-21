from flask import Flask, render_template, request, flash, url_for, jsonify
from bs4 import BeautifulSoup

import os, sys
import requests
import json
from summarizer_wip import *
#from newspaper import Article
#import eatiht.v2 as v2
#dirname = os.path.dirname(sys.argv[0])
#import eatiht

app = Flask(__name__)

word_vector_file = '/home/pk/Downloads/crawl-300d-2M.magnitude'
s = Summarizer(word_vector_file)

@app.route('/summarize', methods=['POST'])
def summarize():
    print('in summarize route')
    req_data = request.get_json()
    text = req_data['text']
    number_of_sentences = req_data['num']
    option = req_data['option']

    if option == 'text':
        text = text
    elif option == 'url':
        text = url_to_string(text)

    print(number_of_sentences)

    summarized_text = ".\n".join(s.summarize(text, number_of_sentences))

    td = {'outputtext' : summarized_text}

    return jsonify(td)


def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))



if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 6000, debug=True)



# def get_html(url):
#     return url #eatiht.extract(url)
#
#
#
# @app.route('/', method='GET')
# @app.route('/', method='POST')
# def index():
#     search_results = {}
#     summarized_text = ""
#     original_text = ""
#     if request.method == "POST":
#         url = request.forms.get('url')
#         sen_num = int(request.forms.get('sen_num'))
#         original_text = get_html(url)
#         summarized_text = ".\n".join(s.summarize(original_text, sen_num))
#   #      print(search_results)
#     return template('index.html', original_text=original_text, summarized_text = summarized_text)
#
#
# @app.route('/summarize/<length:int>/<url:path>', method='GET')
# def summarize(length, url):
#         original_text = get_html(url)
#         summarized_text = ".\n".join(s.summarize(original_text, length))
#         response.content_type = 'application/json'
#         return json.dumps({'original':original_text, 'summarized':summarized_text})
#   #      print(search_results)
#
#
# @app.route('/static/<filename:path>')
# def send_static(filename):
#     static_f = static_file(filename, root='static/')
#     return static_f
#
# if __name__ == '__main__':
#     run(app, host='0.0.0.0', port=sys.argv[1])
