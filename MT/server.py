#!/usr/bin/env python
import configargparse

import json
import re
import os
from onmt.translate import TranslationServer, ServerModelError
from flask import Flask, jsonify, request,render_template,redirect, url_for
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

STATUS_OK = "ok"
STATUS_ERROR = "error"


def start(config_file,
          url_root="./translator",
          host="0.0.0.0",
          port=5000,
          debug=True):

    app = Flask(__name__,)
    translation_server = TranslationServer()
    translation_server.start(config_file)
    
    @app.route('/translate', methods=['POST'])
    def translate():
        paragraphInput = request.get_json(force=True)
        listOfTokenizedSentences, mtSystemID = preprocessingInput(paragraphInput)
        translatedInput = translation(listOfTokenizedSentences, mtSystemID)
        return translatedInput

    def preprocessingInput(paragraphInput):
    	listOfTokenizedSentences = tokenizer(paragraphInput)
    	mtSystemID = int(paragraphInput[0]['id'])
    	return listOfTokenizedSentences, mtSystemID

    def tokenizer(paragraphInput):
        tokenizeParaIntoSentences = sent_tokenize(paragraphInput[0]['src'])
        listOfTokenizedSentences = wordTokenizer(tokenizeParaIntoSentences,int(paragraphInput[0]['id']))
        return listOfTokenizedSentences
    
    def wordTokenizer(tokenizeParaIntoSentences, mtSystemID):
        #Separate word tokenization scheme based on data preprocessing steps taken while training model.
        if mtSystemID==100:
            listOfTokenizedSentences = [" ".join(word_tokenize(sentence.lower())) for sentence in tokenizeParaIntoSentences]
        else:
            listOfTokenizedSentences = [" ".join(word_tokenize(sentence)) for sentence in tokenizeParaIntoSentences]
        return listOfTokenizedSentences

    def translation(listOfTokenizedSentences, mtSystemID):
        inputToserver = [{'id':mtSystemID}]
        outputFromServer={}
        for sentence in listOfTokenizedSentences:
            inputToserver[0]['src']=sentence
            output = {}
            try:
                  translation, scores, n_best, times = translation_server.run(inputToserver)
                  assert len(translation) == len(inputToserver)
                  assert len(scores) == len(inputToserver)
                  output = [{"src": inputToserver[i]['src'], "tgt": translation[i],
                        "n_best": n_best,
                        "pred_score": scores[i]}
                        for i in range(len(translation))]
            except ServerModelError as e:
                  output['error'] = str(e)
                  output['status'] = STATUS_ERROR
            if 'src' not in outputFromServer:
                  outputFromServer['src']=[output[0]['src']]
                  outputFromServer['tgt']=[output[0]['tgt']]
            else:
                  outputFromServer['src'].append(output[0]['src'])
                  outputFromServer['tgt'].append(output[0]['tgt'])
        outputFromServer['src']="\n\n".join(outputFromServer['src'])
        outputFromServer['tgt']="\n\n".join(outputFromServer['tgt'])
        return jsonify(outputFromServer)

    @app.route('/')
    def home():
        out={'src':'','tgt':''}
        return jsonify(out)

    app.run(debug=debug, host=host, port=port, use_reloader=False,
            threaded=True)

def _get_parser():
    parser = configargparse.ArgumentParser(
            config_file_parser_class=configargparse.YAMLConfigFileParser,
        description="NMT RestAPI Server")
    parser.add_argument("--ip", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default="5000")
    parser.add_argument("--url_root", type=str, default="/translator")
    parser.add_argument("--debug", "-d", action="store_true")
    parser.add_argument("--config", "-c", type=str,default="./available_models/transConf.json")
    
    return parser


if __name__ == '__main__':
    parser = _get_parser()
    args = parser.parse_args()
    ip = args.ip
    start(args.config, url_root=args.url_root, host=args.ip, port=args.port,debug=args.debug)
