> To run "Sentiment Analysis" model type below command
	[python3] [SentimentAnalysis.py] [modelType] [Input Sentence]
	* modelType: 1-NormalSentimentAnalysis 2-CodeMixedSentimentAnalysis

> Folders information:
	* Data folder contains datasets for Code Mixed Sentiment Analysis
	* Pickle folder contains already trained models

> To get trained model use this CM_Sentiment.ipynb. For individual models: English-SentimentAnalysisEnglish.py, Hinglish-SentimentAnalysisCodeMixed.py

> For English Sentiment Analysis used the combination of "Textblob and Vader NLTK models". f1-score of Vader model on social media is 0.96
> For Hinglish Code Mixed Sentiment Analysis used the Multi Layer Perceptron with Tfidf word based vectors. This MLP model outperforms other classification algorithms. f1-score of MLP model on IIITH-Social Media dataset 0.6746
