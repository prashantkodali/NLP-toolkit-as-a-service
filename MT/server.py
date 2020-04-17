#!/usr/bin/env python
import configargparse

from flask import Flask, jsonify, request,render_template,redirect, url_for
from onmt.translate import TranslationServer, ServerModelError
import json
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
import re
import os
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

#ip = os.environ['ipVisibleToOutside']
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
        #inputs = request.get_json(force=True)
        inputs=[request.form.to_dict()]
        print(inputs)
        originalInput = inputs[0]['src']
        sentences=sent_tokenize(inputs[0]['src'])
        #sentences=[]
        if int(inputs[0]['id'])==100:
          tok_src=[" ".join(word_tokenize(x.lower())) for x in sentences]
        else:
          tok_src=[" ".join(word_tokenize(x)) for x in sentences]
        print ('input recieved')
        inputs[0]['id']=int(inputs[0]['id'])
        tok_tgt={}
        for sent in tok_src:
            inputs[0]['src']=sent
            out = {}
            try:
                  translation, scores, n_best, times = translation_server.run(inputs)
                  assert len(translation) == len(inputs)
                  assert len(scores) == len(inputs)
                  out = [{"src": inputs[i]['src'], "tgt": translation[i],
                        "n_best": n_best,
                        "pred_score": scores[i]}
                        for i in range(len(translation))]
            except ServerModelError as e:
                  out['error'] = str(e)
                  out['status'] = STATUS_ERROR
            #print(out[0]['tgt'])
            print ('translation done')
            if 'src' not in tok_tgt:
                  tok_tgt['src']=[out[0]['src']]
                  tok_tgt['tgt']=[out[0]['tgt']]
            else:
                  tok_tgt['src'].append(out[0]['src'])
                  tok_tgt['tgt'].append(out[0]['tgt'])
        tok_tgt['src']=originalInput#" ".join(" ".join(tok_tgt['src']).strip().split())
        tok_tgt['tgt']="\n".join(tok_tgt['tgt'])
        tok_tgt['ipVisibleToOutside']=ip
        #return jsonify(translation[0])
        #return redirect(url_for(home, value=out[0]))
        return render_template("index.html", value=tok_tgt)
        #return out[0]['tgt']
    
    @app.route('/')
    def home():
        #if request.args.get('value'):
        #        out={'src':value['src'],'tgt':value['tgt']}
        #else:
        out={'src':'','tgt':'', 'ipVisibleToOutside':ip}
        return render_template('index.html',value=out)
    app.run(debug=debug, host=host, port=port, use_reloader=False,
            threaded=True)


def _get_parser():
    parser = configargparse.ArgumentParser(
        config_file_parser_class=configargparse.YAMLConfigFileParser,
        description="OpenNMT-py REST Server")
    parser.add_argument("--ip", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default="5000")
    parser.add_argument("--url_root", type=str, default="/translator")
    parser.add_argument("--debug", "-d", action="store_true")
    parser.add_argument("--config", "-c", type=str,default="./available_models/conf.json")
    
    return parser


if __name__ == '__main__':
    parser = _get_parser()
    args = parser.parse_args()
    ip = args.ip
    start(args.config, url_root=args.url_root, host=args.ip, port=args.port,
          debug=args.debug)
