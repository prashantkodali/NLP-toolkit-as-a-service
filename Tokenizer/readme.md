### Prerequisite for the application
  
NLTK </br>
```bash
    - pip install nltk 
```
Flask </br>
```bash
    - pip install Flask
```
Regex </br>
```bash
    - pip install re
```

### What is Tokenization?

Tokenization is a very common task in NLP, it is basically a task of chopping a character into pieces, called as token, and throwing away the certain characters at the same time, like punctuation.

The tokens may be words or number or punctuation mark. Tokenization does this task by locating word boundaries. Ending point of a word and beginning of the next word is called word boundaries. These tokens are very useful for finding such patterns as well as is considered as a base step for stemming and lemmatization.

#### Trained Corpus 
- [Bert Large Uncased Vocabulary] ( https://s3.amazonaws.com/models.huggingface.co/bert/bert-large-uncased-vocab.txt)

#### Other Available Corpus 
- [Bert Large Cased Vocabulary] ( https://s3.amazonaws.com/models.huggingface.co/bert/bert-large-cased-vocab.txt)
- [Bert Base Uncased Vocabulary] (https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-vocab.txt)
- [Bert Base Cased Vocabulary] (https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-cased-vocab.txt)

##### Examples: 
  | Input       | Outout     | 
  | ------------- |:-------------:|
  | We need small heroes so that big heroes can shine   | ['[CLS]', 'we', 'need', 'small', 'heroes', 'so', 'that', 'big', 'heroes', 'can', 'shine', '[SEP]'] | 
  | Tokenization is a very common task in NLP      |  ['[CLS]', 'token', '##ization', 'is', 'a', 'very', 'common', 'task', '[SEP]'] | 
  
  
### References
- Packages
  - [Build and Deploy a web-application using Flask](https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/)
  - [Flask](https://flask.palletsprojects.com/en/1.1.x/)

- Papers
  - [Hugging Face Transformer](https://arxiv.org/abs/1910.03771)
  - [NLTK](https://www.researchgate.net/publication/220482883_NLTK_the_Natural_Language_Toolkit)