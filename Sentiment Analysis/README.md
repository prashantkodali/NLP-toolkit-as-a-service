### Introduction About Sentiment Analysis

Sentiment Analysis (SA) is the interpretation and classification of sentiment (positive, negative and neutral) within text data using text analysis techniques. A sentiment analysis system for text analysis combines natural language processing (NLP) and machine learning techniques to assign weighted sentiment scores to the entities, topics, themes and categories within a sentence or phrase.

Our sentiment analysis model detect polarity score within a given text, based on the polarity score model assigns a sentiment label. Here for our model used the coarse-grained sentiment anaysis lables those are Positive, Negative, Neutral. In this NLP-as-a-toolkit service we are building the SA model for normal English text and Hinglish (Hindi and English Code-Mixed data) text. To build the model for nomal English text used the open-source libraries **TextBlob** and NLTK's **VADER** (Valence Aware Dictionary and sEntiment Reasoner) and for Code-Mixed text used the **MultiLayer Perceptron (MLP) with TFIDF vectors**.


#### Model for Normal Text

We'll give the input text for TextBlob and VADER. Each model predict a sentiment label score. Based on that score we will assign maximum scored label to input text.

##### Examples: 
  | Input       | VADER Score      | TextBlob Score  | Output Label |
  | ------------- |:-------------:| -----:| -----------|
  | VADER is VERY SMART, handsome, and FUNNY   | 0.63 | 0.578 | Positive |
  | A really bad, horrible book.      |  -0.432 |  -0.231 | Negative |
  
  positive sentiment: score >= 0.5,
  neutral sentiment:  score > -0.5 and score < 0.5,
  negative sentiment: score <= -0.5
  
#### Model for Code-Mixed Text

For this text we built the Multilayer Perceptron model with word level TF-IDF vectors. And this model is trained on IIITH Hindi English code-mixed data which contains around 13000 tweets. First, We converted the each tweet in the dataset into a d-dimensional word level TF-IDF vector format. These vector representations fed to MLP to predict the label. 

##### Examples
 | Input       | Actual Label      | Predicted Label  
  | ------------- |:-------------: -----------|
  | Trailer dhannnsu hai bhai   | Positive | Positive |
  | abe kutte tere se kon baat karega |  Negative | Negative |

### Results

| Model        | precision      | Recall  | f1-score |
| ------------- |:-------------:| -----:| -----------|
| TextBlob      | 0.75 | 0.74 | 0.76
| VADER      | 0.8      |  0.8 |  0.8 |
| MLP | 0.6505 | 0.6433 | 0.6575 |


### References
