# Machine Translation System

### Short Description of Service

Machine Translation system is a program/model for translating from source language (e.g. English) to target language (e.g. Hindi). There are multiple ways of making such a system e.g. rule based, data driven techniques which make use of ML algorithms, hybrid systems unifying both rule based and data driven based techniques. We are have used ML based models for building MT systems for translating English to Hindi or Bhojpuri. 

### Resources Used to Make MT Systems

#### For Training Machine Translation system

We used [Opennmt](https://github.com/OpenNMT/OpenNMT-py) package to train Neural Machine Translation models. And [Flask](https://github.com/pallets/flask) package for providing APIs for translation service.

#### Data Resources
Models provided as serivce are trained on 2 language pairs English ==> {Hindi, Bhojpuri} using following datasets

- [English Hindi Parallel Corpus v2.1](http://www.cfilt.iitb.ac.in/iitb_parallel/)

- [English Bhojpuri Parallel Corpus](https://sites.google.com/view/loresmt)

#### System Architectures Used

Two architectures were used for training translation models - Attention and Transformer model. For English to Hindi translation model we used both aforementioned models. And for English to Bhojpuri only Attention model was used, since its dataset was very small. And transformer requires more instance to learn translation when compared to attention. Given below is small description of these models, for more comprehensive literature kindly go through reference section.

- Attention Architecture
	![alt text](img/bahdanau.JPG)
	* Bahdanau Attention for translation taken from here*
	![alt text](img/luong.JPG)
	* Luong Attention for translation taken from here*

		figure1 and figure 2

	- Transformer Architecture
		figure 3,4,5?????


#### Results 

Translation systems are evaluated based on how well they perform translation. We are including BLEU scores evaluated off WMT14 newstestset for english hindi and loresmt 2019 testset for english bhojpuri. These scores again provide us a benchmark with whom we can compare future models while including them in translation service.

### Usage of MT service

We made use of flask and opennmt to create RESTful API services which can be called for translating a text in source language (english) into target language (hindi, bhojpuri).

#### MT service pipeline

	UML class diagram
	UML Use case diagram
	UML Flow chart diagram

### References

	- Opennmt
	- iit bombady enlgish hindi parallel corpus
	- jointly learning to aligna and translation
	- attention is all you need
	- a3-108 system submission
	- Bleu Score
	- flask
