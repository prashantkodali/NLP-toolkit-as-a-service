from flask import Blueprint, render_template, request
import requests
from . import db


services = Blueprint('services', __name__)



@services.route('/tokenizer_page',methods = ['GET'])
def tokenizer_page():
    return render_template('pages/tokenize.html')


@services.route('/tokenize_call',methods = ['POST'])
def tokenize_call():
    text = request.form['text']
    td = {'text':text }
    response = requests.post("http://192.168.1.6:5000/ntlktokenize", json = td)

    print(response.json())

    return response.json()
    # return 'Tokenized text: {}'.format(word_tokenize(text))
