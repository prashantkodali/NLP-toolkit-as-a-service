'''
This file is a Blueprint consisting of all flask routes needed for calling services related pages and API endpoints.

Each service has two routes:
1. one for the frontend page, which when called will render the template page for that services. This template will have form for
sourcing the necessary data from the user.
2. another for calling the API end point of each endpoint. Reads the necessary input data from the user, puts it into json. Uses
requests package to hit the api with necessary payload (json) and gets reponse from the service.
'''

from flask import Blueprint, render_template, request, jsonify, flash
import requests
from . import db


services = Blueprint('services', __name__)


####################################################################################################
#Routes for Tokenization service.
@services.route('/tokenizer_page',methods = ['GET'])
def tokenizer_page():
    return render_template('pages/tokenize_ajaxtest.html')


@services.route('/tokenize_call',methods = ['POST'])
def tokenize_call():
    text = request.form['text']
    id = request.form['id']
    td = {'input_text':text, 'id':id }
    response = requests.post("http://e0cd242b.ngrok.io/gettokenizer", json = td)

    return render_template('pages/tokenize_ajaxtest.html',input = text, output= response.json()['output_text'])


####################################################################################################
#Routes for Machine Translation service.

@services.route('/mt_page',methods = ['GET'])
def mt_page():
    return render_template('pages/mt.html')


@services.route('/mt_call',methods = ['POST'])
def mt_call():
    src = request.form['src']
    id = request.form['id']
    td = [{'src':src, 'id':id }]
    response = requests.post("http://8ea2b9ff.ngrok.io/translate", json = td)

    print("printing response:\n")
    print(response.json())

    if response.json()['error'] != 'None':
        flash(response.json()['error'])
        return render_template('pages/mt.html', input= response.json()['src'],)

    return render_template('pages/mt.html', input= response.json()['src'], output=response.json()['tgt'])


####################################################################################################
#Routes for Named Entity Recognition service.

@services.route('/ner_page',methods = ['GET'])
def ner_page():
    return render_template('pages/ner.html')

@services.route('/ner_call',methods = ['POST'])
def ner_call():

    if(str(request.form["url_ip"])):
        text = str(request.form["url_ip"])
        type = "url"
        td = {'text':text, 'type':type }
        response = requests.post("http://38892c1c.ngrok.io/getNER", json = td)

    elif(str(request.form["txt_ip"])):
        text = str(request.form["txt_ip"])
        type = "text"
        td = {"text":text, "type":type }

        print(td)

        response = requests.post("http://38892c1c.ngrok.io/getNER", json = td)

        print(response.json()['output_text'])

    return render_template('pages/ner.html', tags= response.json()['output_text'])


####################################################################################################
#Routes for Text Representation service.

@services.route('/emb_page',methods = ['GET'])
def emb_page():
    return render_template('pages/emb.html')

@services.route('/emb_call',methods = ['POST'])
def emb_call():

    text = request.form['txt_ip']
    id = request.form['id']

    td = {'text':text, 'id':id}

    response = requests.post("https://7a7645ae.ngrok.io/GenerateEmbeddings", json = td)

    print(response.json()['embeddings'])

    return render_template('pages/emb.html', output= response.json()['embeddings'])


####################################################################################################
#Routes for Sentiment Analysis service.

@services.route('/sentiment_page',methods = ['GET'])
def sentiment_page():
    return render_template('pages/sentiment.html')

@services.route('/sentiment_call',methods = ['POST'])
def sentiment_call():

    text = request.form['txt_ip']
    id = int(request.form['id'])

    td = {'text':text, 'id':id,}

    response = requests.post("http://8dc45a7f.ngrok.io/getSentiment", json = td)

    return render_template('pages/sentiment.html', input = text,output= response.json()['label'])

####################################################################################################
#Routes for Summarization service.

@services.route('/summarize_page',methods = ['GET'])
def summarize_page():
    return render_template('pages/summarization.html')

@services.route('/summarize_call',methods = ['POST'])
def summarize_call():

    text = request.form['text']
    num = int(request.form['num'])

    td = {'text':text, 'num':num}

    response = requests.post("http://localhost:6000/summarize", json = td)

    return render_template('pages/summarization.html', input = text, sen_num = num, output= response.json()['outputtext'])


####################################################################################################
#Routes for Transliteration service.


@services.route('/transliteration_page',methods = ['GET'])
def transliteration_page():
    return render_template('pages/transliteration.html')

@services.route('/transliteration_call',methods = ['POST'])
def transliteration_call():

    text = request.form['text']

    td = {'text':text}

    response = requests.post("http://localhost:7000/transliterate", json = td)

    return render_template('pages/transliteration.html', input = text, output= response.json()['transliterated_text'])
