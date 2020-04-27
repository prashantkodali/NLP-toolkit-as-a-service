## <p align="center"> <b> Extractive Summarization</b><br></p>

In this service we have deployed a k-means bases summarization using FastText word embeddings for getting sentence Representations.

The service takes following inputs, in a JSON format:
- Input text, for which summary is to be generated.
- Number of sentences in summary

The service outputs the following in json format:
- Summary of the input text in the number of sentences as mentioned in the inputText
- error in case any of the input validation cases fail.


Following is the brief summary of the algorithm used for generating the summary:

1. Sentence tokenize the input text, using a simple regular expression pattern.
2. Generate sentence Representations for each sentence using pretrained FastText embeddings.
  - for each word in a sentence query the embeddings from pretrained FastText embeddings
  - sum up the embeddings of all words in a sentence to get the sentence embeddings.
3. Run a k-means clustring algorithm to extract n clusters, where n is number of sentences in summary, which is taken as input.
4. Centroids of each cluster are Representative of summary.
5. Pick the nearest sentence to each of the Centroids. String these sentences together to get summary.

The code base for this service uses [Pymagnitue](https://github.com/plasticityai/magnitude) for handling the pretrained word embedding file. This ensures that query time for each word is very less and main memory footprint for these word embeddings is very less.

### <p><b><u>Components</u></b><br></p>
Code base of this service consists of three files:
1. main.py: here flask component of the service is kept, which orchestrates the whole summarizaotn process by calling the following pieces of code. File path to the pretrained word embeddings is defined in this file. Has to be changed to indicate path to the embedding file in the system where the service is to be run.
2. errorCheck.py: implements the class for error checking. Currently two error handling cases, as described above, are added. Additional error test cases can be added to this class. There is a method in this class, called CheckInput() which orchestrates each error case check. Writing a seperate class ensures that we can add more test cases without much change to code base.
4. summarizer.py: A class implemnted which does the actual summarization. Method followed in this code is same as described above.

-----

### How to Run the app
1. Packages needed to run these services are:
- Flask
- PyMagnitude for quick loading of pretrained word embeddings.
- Magnitude needs word embeddings in .magnitude format for quick loading. Any .bin or .vec file can be converted into .mangnitude format using pymagnitude package. Please refer [Pymagnitue](https://github.com/plasticityai/magnitude) for conversion.
- Sklearn for K-means clustering.

2. Flask service written in main.py is configured to run by port 7000 in main.py. If the user wants to change user can change in main.py, where run() method is being called on the flask app.
3. To run the service just run
```$flask main.py
```
