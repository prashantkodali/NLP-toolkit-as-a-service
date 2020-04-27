# Automatic Machine Translation Output Evaluation.

This service can be added by using 'Add Service' option with admin rights. 

### To start the server 

To start server kindly use following command, 

```bash
 python serverMTEval.py
```

### Prerequisite for Server

Flask </br>
```bash
     -pip install Flask
```

### Short Description of Service

Machine Translation (MT) is the task of converting the source text in one natural language to another natural language by preserving both faithfulness and fluency. MT output can be evaluated by both humans and automatic evaluation metrics. Whereas, human judgements are more reliable, they are expensive and time-consuming.
BLEU and NIST are the widely used automatic evaluation metrics which follow the idea of n-gram matching between the candidate sentence and the reference sentence.

This online Automatic MT Evaluation service uses NLTK package to retrieve the Scores.  </br>
Note: Reference Sentence and Hypothesis Sentences should be provided by the end user.  </br>
Reference Sentence  : Gold/True Sentence </br>
Hypothesis Sentence : Translated Sentence for which score needs to be computed. </br>


Example Usage:
	
	curl -i -H "Content-Type: application/json" -X POST -d "{\"hyp\":\"Amy is a American. She came to India yesterday. She works for Google.\", \"ref\":\"Amy is a American. She came to India yesterday. She works for Google.\"}" 127.0.0.1:8000/getMTEval
	127.0.0.1:8000 --> Local host server can be made publicly available using ngrok [https://ngrok.com/]
 
	JSON Output: 
 {
  "bleu": [
    1.1167470964180197
  ],
  "error": null,
  "nist": [
    3.713260230961604
  ]
}
	

Input Parameters : Json (hyp,ref)

	| Field | Type    | Description                                                         |
	|-------|---------|---------------------------------------------------------------------|
	| hyp   | String  | Hypothesis Sentences                                                |
	| ref   | String  | Reference Sentences                                                 |
	|-------|---------|---------------------------------------------------------------------|

Output : Json File (bleu, nist, errorMessage)

	| Field        | Type   | Description                                                                     |
	|--------------|--------|---------------------------------------------------------------------------------|
	| bleu         | float  | BLEU Score                                                                      |
	| nist         | float  | NIST Score                                                                      |
	| error        | String | Contains error message, if any.                                                 |
	|--------------|--------|---------------------------------------------------------------------------------|



### References

- Packages
	- [BLEU SCORE](https://www.nltk.org/_modules/nltk/translate/bleu_score.html)
	- [NIST SCORE](https://www.nltk.org/_modules/nltk/translate/nist_score.html)
	- [ngrok](https://ngrok.com/)
- Reference Papers
	- [BLEU: a Method for Automatic Evaluation of Machine Translation](https://www.aclweb.org/anthology/P02-1040.pdf) 
 - [Automatic evaluation of machine translation quality using n-gram co-occurrence statistics](https://dl.acm.org/doi/10.5555/1289189.1289273)
