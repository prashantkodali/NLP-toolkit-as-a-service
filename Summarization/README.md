<p align="center">
  <b>### Extractive Summarization</b><br>
</p>

In this service we have deployed a k-means bases summarization using FastText word embeddings for getting sentence Representations.

The service takes following inputs, in a JSON format:
- Input text, for which summary is to be generated.
- Number of sentences in summary

The service outputs the following:
- Summary of the input text in the number of sentences as mentioned in the inputText


Following is the brief summary of the algorithm used for generating the summary:

1. Sentence tokenize the input text, using a simple regular expression pattern.
2. Generate sentence Representations for each sentence using pretrained FastText embeddings.
  - for each word in a sentence query the embeddings from pretrained FastText embeddings
  - sum up the embeddings of all words in a sentence to get the sentence embeddings.
3. Run a k-means clustring algorithm to extract n clusters, where n is number of sentences in summary, which is taken as input.
4. Centroids of each cluster are Representative of summary.
5. Pick the nearest sentence to each of the Centroids. String these sentences together to get summary.

The code base for this service uses [Pymagnitue](https://github.com/plasticityai/magnitude) for handling the pretrained word embedding file. This ensures that query time for each word is very less and main memory footprint for these word embeddings is very less. 
