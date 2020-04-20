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

@services.route('/ner_page',methods = ['GET'])
def ner_page():
    return render_template('pages/ner.html')

@services.route('/ner_call',methods = ['POST'])
def ner_call():

    if(str(request.form["url_ip"])):
        text = str(request.form["url_ip"])
        type = "url"
        td = {'text':text, 'type':type }
        response = requests.post("http://45db40b2.ngrok.io/getNER", json = td)

    elif(str(request.form["txt_ip"])):
        text = str(request.form["txt_ip"])
        type = "text"
        td = {'text':text, 'type':type }

        response = requests.post("http://45db40b2.ngrok.io/getNER", json = td)


    # print(response.json())
    return render_template('pages/ner.html', tags= response.json()['output_text'])



@services.route('/emb_page',methods = ['GET'])
def emb_page():
    return render_template('pages/emb.html')

@services.route('/emb_call',methods = ['POST'])
def emb_call():

    text = request.form['txt_ip']
    id = request.form['id']

    td = {'text':text, 'id':id}

    response = requests.post("http://4063843b.ngrok.io/GenerateEmbeddings", json = td)
    print(response.json()['embeddings'])
    # print(response.json())
    return render_template('pages/emb.html', tags= response.json()['embeddings'])
