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
from .models_db import Service


services = Blueprint('services', __name__)


def getservices():

    servicesall = Service.query.all()

    services = []

    for service in servicesall:
        services.append([service.service_page_call, service.service_name])

    return services

####################################################################################################
#Routes for Tokenization service.
@services.route('/tokenizer_page',methods = ['GET'])
def tokenizer_page():
    return render_template('pages/tokenize_ajaxtest.html', services = getservices())


@services.route('/tokenize_call',methods = ['POST'])
def tokenize_call():
    text = request.form['text']
    id = request.form['id']
    td = {'input_text':text, 'id':id }

    service = Service.query.filter_by(service_service_call = '/tokenize_call').first()
    apiendpoint = service.service_api_endpoint

    try:
        response = requests.post(apiendpoint, json = td)

        if response.json()['error'] != 'None':
            flash(response.json()['error'])
            return render_template('pages/tokenize_ajaxtest.html', input= text,services = getservices())
        return render_template('pages/tokenize_ajaxtest.html',input = text, output= response.json()['output_text'], services = getservices())

    except Exception as e:
        flash("There seems to be a issue with the service. Please contact the admin.")
        return render_template('pages/tokenize_ajaxtest.html', input= text, services = getservices(), flash = "There seems to be a issue with the service. Please contact the admin.")

####################################################################################################
#Routes for Machine Translation service.

@services.route('/mt_page',methods = ['GET'])
def mt_page():
    return render_template('pages/mt.html', services = getservices())


@services.route('/mt_call',methods = ['POST'])
def mt_call():
    src = request.form['src']
    id = request.form['id']
    td = [{'src':src, 'id':id }]

    service = Service.query.filter_by(service_service_call = '/mt_call').first()
    apiendpoint = service.service_api_endpoint


    response = requests.post(apiendpoint, json = td)


    try:
        if response.json()['error'] != 'None':
            flash(response.json()['error'])
            return render_template('pages/mt.html', input= response.json()['src'],services = getservices())

        return render_template('pages/mt.html', input= response.json()['src'], output=response.json()['tgt'], services = getservices())
    except :
        flash("There seems to be a issue with the service. Please contact the admin.")
        return render_template('pages/mt.html', input= text, services = getservices(), flash = "There seems to be a issue with the service. Please contact the admin.")

####################################################################################################
#Routes for Named Entity Recognition service.

@services.route('/ner_page',methods = ['GET'])
def ner_page():
    return render_template('pages/ner.html', services = getservices())

@services.route('/ner_call',methods = ['POST'])
def ner_call():

    service = Service.query.filter_by(service_service_call = '/ner_call').first()
    apiendpoint = service.service_api_endpoint

    if(str(request.form["url_ip"])):
        text = str(request.form["url_ip"])
        type = "url"
        td = {'text':text, 'type':type }
        response = requests.post(apiendpoint, json = td)

    elif(str(request.form["txt_ip"])):
        text = str(request.form["txt_ip"])
        type = "text"
        td = {"text":text, "type":type }

        response = requests.post(apiendpoint, json = td)

    # print(response.json())
    try:
        if response.json()['error'] != None:
            flash(response.json()['error'])
            return render_template('pages/ner.html', input= text, services = getservices())

        return render_template('pages/ner.html',services = getservices(), tags= response.json()['output_text'], annotatedTag = response.json()['annotated_tags'])

        # return render_template('pages/ner.html', input= text, tags= response.json()['output_text'], annotatedTag = str(response.json()['annotated_tags']))

    except :
        flash("There seems to be a issue with the service. Please contact the admin.")
        return render_template('pages/ner.html', input= text, services = getservices(), flash = "There seems to be a issue with the service. Please contact the admin.")
####################################################################################################
#Routes for Text Representation service.

@services.route('/emb_page',methods = ['GET'])
def emb_page():
    return render_template('pages/emb.html', services = getservices())

@services.route('/emb_call',methods = ['POST'])
def emb_call():

    text = request.form['txt_ip']
    id = request.form['id']

    td = {'text':text, 'id':id}

    service = Service.query.filter_by(service_service_call = '/emb_call').first()
    apiendpoint = service.service_api_endpoint

    response = requests.post(apiendpoint, json = td)

    try:
        if response.json()['error'] != 'None':
            flash(response.json()['error'])
            return render_template('pages/emb.html', input= response.json()['embeddings'],services = getservices())


        return render_template('pages/emb.html', input_text= text,  output= response.json()['embeddings'],services = getservices())

    except :
        flash("There seems to be a issue with the service. Please contact the admin.")
        return render_template('pages/emb.html', input_text= text, services = getservices(), flash = "There seems to be a issue with the service. Please contact the admin.")


####################################################################################################
#Routes for Sentiment Analysis service.

@services.route('/sentiment_page',methods = ['GET'])
def sentiment_page():
    return render_template('pages/sentiment.html', services = getservices())

@services.route('/sentiment_call',methods = ['POST'])
def sentiment_call():

    text = request.form['txt_ip']
    id = int(request.form['id'])

    td = {'text':text, 'id':id}

    service = Service.query.filter_by(service_service_call = '/sentiment_call').first()
    apiendpoint = service.service_api_endpoint

    response = requests.post(apiendpoint, json = td)

    try:
        response = requests.post(apiendpoint, json = td)
        return render_template('pages/sentiment.html', input = text,output= response.json()['label'],services = getservices())
    except :
        flash("There seems to be a issue with the service. Please contact the admin.")
        return render_template('pages/sentiment.html', input= text, services = getservices(), flash = "There seems to be a issue with the service. Please contact the admin.")


####################################################################################################
#Routes for Summarization service.

@services.route('/summarize_page',methods = ['GET'])
def summarize_page():
    return render_template('pages/summarization.html', services = getservices())

@services.route('/summarize_call',methods = ['POST'])
def summarize_call():

    text = request.form['text']

    try:
        num = int(request.form['num'])
    except Exception as e: #for handling case when the input is either not a number or empty.
        flash("Please enter number of sentences.")
        return render_template('pages/summarization.html', input = text, sen_num = "None", output= "None", services = getservices())


    td = {'text':text, 'num':num}

    service = Service.query.filter_by(service_service_call = '/summarize_call').first()
    apiendpoint = service.service_api_endpoint

    try:
        response = requests.post(apiendpoint, json = td)

        if response.json()['error'] != 'None':
            flash(response.json()['error'])
            return render_template('pages/summarization.html', input = text, sen_num = num, output= "None", services = getservices())

        return render_template('pages/summarization.html', input = text, sen_num = num, output= response.json()['outputtext'], services = getservices())
    except :
        flash("There seems to be a issue with the service. Please contact the admin.")
        return render_template('pages/summarization.html', input= text, services = getservices(), flash = "There seems to be a issue with the service. Please contact the admin.")


####################################################################################################
#Routes for Transliteration service.


@services.route('/transliteration_page',methods = ['GET'])
def transliteration_page():
    return render_template('pages/transliteration.html', services = getservices())

@services.route('/transliteration_call',methods = ['POST'])
def transliteration_call():
    text = request.form['text']

    service = Service.query.filter_by(service_service_call = '/transliteration_call').first()
    apiendpoint = service.service_api_endpoint

    td = {'text':text}

    try:
        response = requests.post(apiendpoint, json = td)
        if response.json()['error'] != 'None':
            flash(response.json()['error'])
            return render_template('pages/transliteration.html', input = text, output= "None", services = getservices())

        return render_template('pages/transliteration.html', input = text, output= response.json()['transliterated_text'], services = getservices())
    except :
        flash("There seems to be a issue with the service. Please contact the admin.")
        return render_template('pages/transliteration.html', input= text, services = getservices(), flash = "There seems to be a issue with the service. Please contact the admin.")
