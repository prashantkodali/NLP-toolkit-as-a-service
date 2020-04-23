### Text Representation as a Service

Word Embeddings or Sentence Embeddings are a distributed way of representation for text that allows words and sentences with similar meaning to have a similar representation.The underlying hypothesis in linguistics is derived from the semantic theory of language usage, i.e. words that are used and occur in the same contexts tend to purport similar meanings.
The correlation between distributional and semantic similarity can be operationalized in many ways. Word2Vec and Glove Vectors were based on these distributed semantics and they worked well. However ,many  words  are  semantically  ambiguous,  and  can  refer tomore than one concept.  For example,"bark" can refer either to a part of a tree, or to the sound made by a dog.  To understand such words, we must disambiguate between these different interpretations, normally on the basis of the context in which the word occurs.  

BERT, or Bidirectional Encoder Representations from Transformers, is a method of pre-training language representations, meaning a general-purpose "language understanding" model is trained on a large text corpus (like Wikipedia), and then that model is used for downstream NLP tasks like Sentiment Analysis , Summarization etc. BERT outperforms previous methods because it is the first unsupervised, deeply bidirectional system for pre-training NLP and has also achieved  new  state-of-the-art  results  on Word Sense Disambiguation (WSD).

The paper which describes BERT in detail and provides full results on a number of tasks can be found here: https://arxiv.org/abs/1810.04805.

Lately, several methods have been presented to improve BERT on either its prediction metrics or computational speed, but not both.

1) DistilBERT improves on the inference speed. It learns a distilled (approximate) version of BERT, retaining 97% performance but using only half the number of parameters.
The table below compares them for what they are!


|                | BERT          | DistilBERT | 
| -------------: |:-------------:| -----:| 
|Size(in millions)| Base : 110 | Base : 66 | 
|Training | Base: 8xV100x12 days| Base: 8xV100x3.5 days|
|Performance |Outperforms sata-of-art in Oct 2018|3% degradation from BERT|


2)AlBERT represents a new state of the art for NLP on several benchmarks and new state of the art for parameter efficiency.

|                | BERT          | AlBERT|
| -------------: |:-------------:|--------:|
|Size(in millions)| Base : 110 | Large: 18 |
|Performance |Outperforms sata-of-art in Oct 2018| 1- 5% increase from BERT|


### References
    1. Datasets
       a. [a link](https://github.com/user/repo/blob/branch/other_file.md)
       b. [a link](https://github.com/user/repo/blob/branch/other_file.md)

