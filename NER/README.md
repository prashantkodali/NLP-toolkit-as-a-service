# Named Entity Recognition

### To start the server 

To start server kindly use following command, 

```bash
 python Server_Entry.py
```
Small description of fields is given below,

| Field  | Field Description                                                                                                                                    |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| ip     | ip Address which will be exposed as server. Default: 0.0.0.0                                                                                         |
| port   | port used for handling translation request. Default: 5000                                                                                            |

### Prerequisite for Server
	
Spacy </br>
```bash
    - pip install spacy </br>
    - python -m spacy download en_core_web_sm </br>
```
Flask </br>
```bash
     -pip install Flask
```
	

### Short Description of Service

Description of the service:</u> NER is probably the first step towards information extraction that seeks to locate and classify named entities in text into pre-defined categories such as the names of persons, organizations, locations, expressions of times, quantities, monetary values, percentages, etc. NER is used in many fields in Natural Language Processing.


#### For Training Machine Translation system

This online NER service uses SpaCy’s trained model to identify the named entities. Input can be either in text format or URL.
Note: In case of URL as input, output can be generated only if web-scrapping is permitted for that particular URL.

#### Trained Corpus 
- [OntoNotes Release 5.0] (https://catalog.ldc.upenn.edu/LDC2013T19)

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

#### System Architectures Used


Example Usage:
	
	curl -i -H "Content-Type: application/json" -X POST -d "{\"type\":\"text\", \"text\":\"Amy is a good girl. She came to India yesterday. She works for google.\"}" 127.0.0.1:8080/getNER
	127.0.0.1:8080 --> Local host server can be made publicly available using ngrok [https://ngrok.com/]
  
Input Parameters : Json (src,id)

	| Field | Type    | Description                                                         |
	|-------|---------|---------------------------------------------------------------------|
	| type  | String  | Input type   (url / text)                                           |
	| text  | String  | Input text / Input Url                                              |
	|-------|---------|---------------------------------------------------------------------|

Output : Json File (src, tgt, errorMessage)

	| Field        | Type   | Description                                                                     |
	|--------------|--------|---------------------------------------------------------------------------------|
	| Output Tags  | String | Output with entities marked in html                                             |
	| tags         | String | Output with entities annotated.                                                 |
	| errorMessage | String | Contains error message, if any.                                                 |
	|--------------|--------|---------------------------------------------------------------------------------|



### References

- Packages
	- [Spacy](https://github.com/explosion/spacy-models/releases//tag/en_core_web_sm-2.2.5)
  - [ngrok](https://ngrok.com/)
- Trained Corpus
	- [OntoNotes Release 5.0] (https://catalog.ldc.upenn.edu/LDC2013T19)
- Blogs
	- For Named Entity Recognition [blog](https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da) 
