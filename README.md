# Sentiment Analysis on Electric Vehicles in India using Deep Learning

## Abstract:
The advent of technology has led to the emergence of electric vehicles. These eco-friendly modes of transportation have the potential to reduce pollution and have garnered much attention among consumers. In order to gain insight into consumer opinions and perceptions, it is essential for automotive sales companies to monitor relevant online forums. Using web scraping techniques, we collected data from popular Indian automotive websites and processed it using natural language processing (NLP). To analyse the data, we employed various deep learning techniques such as Convolutional Neural Networks (CNN), Long Short-Term Memory (LSTM), Simple Recurrent Neural Networks (SimpleRNN), Bidirectional Long Short-Term Memory (BiLSTM), and CNN-LSTM. After comparing their accuracies, we found CNN-LSTM to be the most effective deep learning model, with an accuracy of 97.2%. This level of accuracy provides valuable insight into consumer sentiment and can be useful for automotive companies seeking to understand their target audience.

## Introduction:
Electric vehicles serve as a critical means to reduce pollution and provide an eco-friendly alternative to traditional petrol or diesel-based engine vehicles. In India, vehicles are responsible for contributing 20-30% of the air pollution (as stated by the International Energy Agency) [14]. Adopting the use of electric vehicles can significantly reduce this pollution. Additionally, non-renewable resources are rapidly depleting, and as a result, alternative options are necessary to meet our needs. Electric vehicles can serve as a viable alternative to traditional vehicles in India. In fact, the Indian government has recent approved a new $500 million Electric Vehicle (EV) Policy to promote India as a manufacturing hub for EVs and attract investment from global EV manufacturers.

## Method:

![image](https://github.com/user-attachments/assets/0809ae59-7ec8-4ef8-843c-767c1cad8d30)
                                                Fig. 1. Research Method

### 	Data Collection
1.	Target Websites: Identify the top websites in India that focus on reviews related to EVs. Consider including a mix of general automotive sites and those specializing in EVs.
2.	Web Scraping: Utilize web scraping technique s to extract reviews and relevant content from these websites. Used Octoparse, a web scraping tool that allows us to extract data from websites.
Websites:
•	India:
o	Bikewale.com
o	Bikedekho.com
o	Cardekho.com
o	Carwale.com


     ![image](https://github.com/user-attachments/assets/b5247a1f-4451-4e47-8ffa-73c78966c90b)

 
 ### 	Data Preprocessing
1.	Cleaning: Remove irrelevant information like HTML tags, punctuation, and stop words (common words like "the," "a").
2.	Language Processing: Depending on the website language (English or the local language), apply Natural Language Processing (NLP) techniques lemmatization to reduce words to their root form.
3.	Sentiment Labelling: Annotate a small portion of the data (reviews) manually with sentiment labels (positive, negative, neutral) for training a machine learning model.


### Data Analysis 
Dataset consists of  2107 reviews after data cleaning.

![image](https://github.com/user-attachments/assets/c2eabb6f-479f-4198-897a-c1020c5878ab)
 Fig 1. Word Cloud by Sentiment

![image](https://github.com/user-attachments/assets/4196de60-4a3a-40e9-aa17-1a63cacb825b)
                                           Fig 2. Top Positive Reviewers 

 ![image](https://github.com/user-attachments/assets/c4c280b1-2051-4b8b-80a5-87d9ee68e55f)
Fig 3. Sentiment after Analysing the dataset


![image](https://github.com/user-attachments/assets/72ca63c5-0e1a-46e0-bf0e-3cb05b5aa424)
Fig4. Sentiment over Time

### 	Data Preprocessing for NLP
Used one hot encoding and the word2vec for data preprocessing and the feature engineering.
1.	One-hot Encoding: Used to represent categorical data numerically. 
2.	Word2Vec: Used to represent words as dense vectors in a continuous vector space.

### Machine Learning/Deep Learning
1.	Model Selection:. 
o	Machine Learning: Used Naive Bayes.
o	Deep Learning: Used Long Short-Term Memory (LSTM), SimpleRNN, Bidirectional LSTM, CNN and CNN-LSTM.
2.	Training: Train the chosen model using the labelled data.
3.	Evaluation: Evaluate the model's performance on a separate validation dataset to ensure its accuracy. evaluate their performance on the testing data using metrics like accuracy, precision, recall, and F1-score. 

![image](https://github.com/user-attachments/assets/721d8d27-7f35-4ef8-9a67-609d71580dbe)


### Conclusion:
•	We've received 1200 positive reviews on EVs in India, indicating a predominantly favorable sentiment among users. 
•	Sentiment analysis reveals a notable shift over time. Initially, in 2019, there was some negativity surrounding EVs, but as time progressed, this sentiment diminished significantly, transitioning into overwhelmingly positive reviews by 2023. 
•	Among various deep learning models compared, both CNN and CNN-LSTM models exhibited the highest accuracies at 97.16%. Given their strong performance on our dataset, utilizing deep learning for analysis appears advantageous. 
•	In the positive reviews, we observed mentions of eco-friendliness, aesthetics, and overall quality, indicating a strong emphasis on environmental consciousness and satisfaction with the product's appearance and performance.  Conversely, negative reviews primarily highlighted concerns regarding cost and the adequacy of charging infrastructure, underscoring challenges related to affordability and accessibility in the EV market.

•	Policymakers can leverage this analysis to shape policies promoting EV adoption. Insights into consumer concerns can guide efforts addressing challenges such as charging infrastructure development and battery range limitations. 
•	Companies in the EV industry stand to benefit from understanding consumer sentiment. This knowledge enables manufacturers to tailor their products and marketing strategies to better meet customer needs and preferences across different countries.



