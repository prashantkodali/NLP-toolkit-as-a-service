#!/usr/bin/env python
import configargparse

import json
import re
import os
from onmt.translate import TranslationServer, ServerModelError
from flask import Flask, jsonify, request
from mtServerClass import *

STATUS_OK = "ok"
STATUS_ERROR = "error"

def start(config_file,
		  host="0.0.0.0",
		  port=5000,
		  debug=True):

	app = Flask(__name__,)
	mtSystem = translationPipeline('wordNltk','sentNltk',config_file)


	@app.route('/translate', methods=['POST'])
	def translate():
		inputData = request.get_json()
		preprocessedData, modelID, inputError = mtSystem.preprocessingInput(inputData)
		if inputError == "None":
		   	output = mtSystem.translate(preprocessedData, modelID)
		else:
			output = {"src":"\n".join([sentence for sentence in preprocessedData]), "tgt":""}
		output["error"] = inputError

		return jsonify(output)

	app.run(debug=debug, host=host, port=port, use_reloader=False,
			threaded=True)

def _get_parser():
	parser = configargparse.ArgumentParser(
			config_file_parser_class=configargparse.YAMLConfigFileParser,
		description="NMT RestAPI Server")
	parser.add_argument("--ip", type=str, default="0.0.0.0")
	parser.add_argument("--port", type=int, default="5000")
	parser.add_argument("--debug", "-d", action="store_true")
	parser.add_argument("--config", "-c", type=str,default=".mtConf.json")
	
	return parser


if __name__ == '__main__':
	parser = _get_parser()
	args = parser.parse_args()
	start(args.config, host=args.ip, port=args.port,debug=args.debug)
