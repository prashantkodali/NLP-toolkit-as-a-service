from flask import Blueprint, render_template, request, jsonify
import requests
from . import db


services = Blueprint('services', __name__)

@services.route('/tokenizer_page',methods = ['GET'])
def tokenizer_page():
    return render_template('pages/tokenize_ajaxtest.html')


@services.route('/tokenize_call',methods = ['POST'])
def tokenize_call():
    text = request.form['text']
    # text = request.args.get('input_text', 0, type=int)
    print(text)
    td = {'text':text }
    response = requests.post("http://192.168.1.6:5000/ntlktokenize", json = td)

    print(response.json())
    print(type(response.json()))
    print(type(jsonify(response.json())))

    return render_template('pages/tokenize_ajaxtest.html',input = text, output= response.json()['output_text'])
    # return 'Tokenized text: {}'.format(word_tokenize(text))

@services.route('/mt_page',methods = ['GET'])
def mt_page():
    return render_template('pages/mt.html')


@services.route('/mt_call',methods = ['POST'])
def mt_call():
    src = request.form['src']
    id = request.form['id']
    td = [{'src':src, 'id':id }]
    response = requests.post("http://8ea2b9ff.ngrok.io/translate", json = td)

    print(response.json())
    return render_template('pages/mt.html', input= response.json()['src'], output=response.json()['tgt'])
    # return response.json()
    # return 'Tokenized text:
