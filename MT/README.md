# Machine Translation System

 early description 
        attention
        transformer
    api call kaise karna
    references
        papers

### Short Description

	Machine Translation system is a program/model for translating from source language (e.g. English) to target language (e.g. Hindi). There are multiple ways of making such a system e.g. rule based, data driven techniques which make use of ML algorithms, hybrid systems unifying both rule based and data driven based techniques. We are have used ML based models for building MT systems for translating English to Hindi or Bhojpuri. 

### Resources Used to make MT systems

#### For training Machine Translation system
	We used [Opennmt](https://github.com/OpenNMT/OpenNMT-py/) package to train Neural Machine Translation models. 

#### Data Resources
	Models were trained on 2 language pairs English --> {Hindi, Bhojpuri} using following datasets
		- [English Hindi Parallel Corpus v2.1](http://www.cfilt.iitb.ac.in/iitb_parallel/)
		- [English Bhojpuri Parallel Corpus](https://sites.google.com/view/loresmt)

#### System Architectures Used

	- Attention Architecture
		figure1 and figure 2

	- Transformer Architecture
		figure 3,4,5?????


#### Results 

Translation systems are evaluated based on how well they perform translation. We are including BLEU scores evaluated off WMT14 newstestset for english hindi and loresmt 2019 testset for english bhojpuri. These scores again provide us a benchmark with whom we can compare future models while including them in translation service.

### Usage of MT service

We made use of flask and opennmt to create RESTful API services which can be called for translating a text in source language (english) into target language (hindi, bhojpuri).

#### MT service pipeline

	sequential flow of diagram (UML diagram)

### References

	- Opennmt
	- iit bombady enlgish hindi parallel corpus
	- jointly learning to aligna and translation
	- attention is all you need
	- a3-108 system submission
	- Bleu Score
	- flask