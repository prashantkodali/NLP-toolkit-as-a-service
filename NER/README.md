# Named Entity Recognition

### To start the server 

To start server kindly use following command, 

```bash
 python serverEntry.py
```

### Prerequisite for Server
	
Spacy </br>
```bash
    - pip install spacy 
    - python -m spacy download en_core_web_sm 
```
Flask </br>
```bash
     -pip install Flask
```
Beautiful Soup </br>
```bash
     -pip install beautifulsoup4
```
### Short Description of Service

Description of the service:</u> NER is probably the first step towards information extraction that seeks to locate and classify named entities in text into pre-defined categories such as the names of persons, organizations, locations, expressions of times, quantities, monetary values, percentages, etc. NER is used in many fields in Natural Language Processing.

This online NER service uses SpaCy’s trained model to identify the named entities. Input can be either in text format or URL. </br>
Note: In case of URL as input, output can be generated only if web-scrapping (using Beautiful Soup) is permitted for that particular URL.

#### Trained Corpus 
- [OntoNotes Release 5.0](https://catalog.ldc.upenn.edu/LDC2013T19)

#### Entity Types Supported by the Model

 [Named Entity Types](https://spacy.io/api/annotation#section-named-entities)

| TYPE	           | DESCRIPTION	                                                 |
|------------------|---------------------------------------------------------------|
|NORP		           |Nationalities or religious or political groups.	               |
|FAC		           |Buildings, airports, highways, bridges, etc.   	               | 	
|ORG		           |Companies, agencies, institutions, etc.	      	               |
|GPE		           |Countries, cities, states.	                  	               |
|LOC		           |Non-GPE locations, mountain ranges, bodies of water.	         |	
|PRODUCT		       |Objects, vehicles, foods, etc. (Not services.)		             |
|EVENT		         |Named hurricanes, battles, wars, sports events, etc.		       |
|WORK_OF_ART		   |Titles of books, songs, etc.	                 	               |
|LAW		           |Named documents made into laws.	              	               |
|LANGUAGE          |Any named language.	                          	               |
|DATE		           |Absolute or relative dates or periods.	        	             |
|TIME		           |Times smaller than a day.	                  	                 |
|PERCENT	         |Percentage, including ”%“.	                	                 |
|MONEY		         |Monetary values, including unit.	            	               |
|QUANTITY	         |Measurements, as of weight or distance.	       	               |
|ORDINAL	         |“first”, “second”, etc.	                     	                 |
|CARDINAL          |Numerals that do not fall under another type.		               |

#### To Add New Enity Types
For more details on [training](https://spacy.io/usage/training) and updating the named entity recognizer, see the usage guides on training or check out the runnable [training script](https://github.com/explosion/spaCy/blob/master/examples/training/train_ner.py) on GitHub.


#### System Architectures Used

![Flow](https://spacy.io/training-73950e71e6b59678754a87d6cf1481f9.svg)

<b>Training data: </b> Examples and their annotations. </br>
<b>Text: </b>The input text the model should predict a label for. </br>
<b>Label: </b>The label the model should predict. </br>
<b>Gradient: </b> Gradient of the loss function calculating the difference between input and expected output. </br>

Example Usage:
	
	curl -i -H "Content-Type: application/json" -X POST -d "{\"type\":\"text\", \"text\":\"Amy is a American. She came to India yesterday. She works for Google.\"}" 127.0.0.1:8080/getNER
	127.0.0.1:8080 --> Local host server can be made publicly available using ngrok [https://ngrok.com/]
 
	JSON Output: 
	
	{
  	"annotated_tags": "[(Amy, 'PERSON'), (is, ''), (a, ''), (American, 'NORP'), (., ''), (She, ''), (came, ''), (to, ''), (India, 'GPE'), (yesterday, 'DATE'), (., ''), (She, ''), (works, ''), (for, ''), (Google, 'ORG'), (., '')]",
  	"error": null,
  	"output_text": "<div class=\"entities\" style=\"line-height: 2.5\">\n<mark class=\"entity\" style=\"background: #aa9cfc; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone\">\n    Amy\n    <span style=\"font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem\">PERSON</span>\n</mark>\n is a \n<mark class=\"entity\" style=\"background: #c887fb; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone\">\n    American\n    <span style=\"font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem\">NORP</span>\n</mark>\n. She came to \n<mark class=\"entity\" style=\"background: #feca74; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone\">\n    India\n    <span style=\"font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem\">GPE</span>\n</mark>\n \n<mark class=\"entity\" style=\"background: #bfe1d9; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone\">\n    yesterday\n    <span style=\"font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem\">DATE</span>\n</mark>\n. She works for \n<mark class=\"entity\" style=\"background: #7aecec; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone\">\n    Google\n    <span style=\"font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem\">ORG</span>\n</mark>\n.</div>"
	}

Visualising the JSON Output:
![Flow](https://github.com/prashantkodali/NLP-toolkit-as-a-service/blob/master/NER/img/visualizeJSONOutput.png)	


Input Parameters : Json (type,text)

	| Field | Type    | Description                                                         |
	|-------|---------|---------------------------------------------------------------------|
	| type  | String  | Input type   (url / text)                                           |
	| text  | String  | Input text / Input Url                                              |
	|-------|---------|---------------------------------------------------------------------|

Output : Json File (output_text, annotated_tags, errorMessage)

	| Field          | Type   | Description                                                                     |
	|----------------|--------|---------------------------------------------------------------------------------|
	| output_text    | String | Output with entities marked in html                                             |
	| annotated_tags | String | Output with entities annotated.                                                 |
	| errorMessage   | String | Contains error message, if any.                                                 |
	|----------------|--------|---------------------------------------------------------------------------------|



### References

- Packages
	- [Spacy](https://github.com/explosion/spacy-models/releases//tag/en_core_web_sm-2.2.5)
	- [Enchant](http://pyenchant.github.io/pyenchant/)
	- [ngrok](https://ngrok.com/)

- Trained Corpus
	- [OntoNotes Release 5.0](https://catalog.ldc.upenn.edu/LDC2013T19)
- Blogs
	- [Named Entity Recognition](https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da) 
	- [BeautifulSoup](https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python)
	- [Flask](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)
