# -*- coding: utf-8 -*-
"""Electric Vehicle -Sentiment Analysis_India..Colabipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QRo7Hq8xkuOuYhSIjikwx_yoMFk8447s

# **Sentiment Analysis of Electric Vehicles**

## Importing Libraries
"""

import pandas as pd
from textblob import TextBlob

"""## Importing Dataset and Labelling"""

# Read data from Excel file
data = pd.read_excel('EV-Review.xlsx')

# Assuming your dataset has a column named 'Review' containing the reviews
reviews = data['Review'].tolist()

# Function to perform sentiment analysis and assign labels
def analyze_sentiment(review):
    blob = TextBlob(str(review))  # Ensure review is converted to string
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "positive"
    elif sentiment_score < 0:
        return "negative"
    else:
        return "neutral"

# Apply sentiment analysis to each review
data['Sentiment'] = data['Review'].apply(analyze_sentiment)

# Save the labeled dataset back to Excel
data.to_excel('EV_dataset.xlsx', index=False)  # Replace 'labeled_dataset.xlsx' with desired output file path

data = pd.read_excel('EV_dataset.xlsx')

df = pd.DataFrame(data)

"""## Exploratory Data Analysis"""

df.head()

df.shape

df.isnull().sum()

df.shape

df['Sentiment'].value_counts()

df.head(2)

missing_values = df[df['Review'].isnull()]

# @title Word Cloud by Sentiment

import matplotlib.pyplot as plt
from wordcloud import WordCloud
positive_words = ' '.join(df[df['Sentiment'] == 'positive']['Review'].tolist())
negative_words = ' '.join(df[df['Sentiment'] == 'negative']['Review'].tolist())
positive_wordcloud = WordCloud(width=800, height=400).generate(positive_words)
negative_wordcloud = WordCloud(width=800, height=400).generate(negative_words)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(positive_wordcloud, interpolation='bilinear')
plt.title('Positive Reviews')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(negative_wordcloud, interpolation='bilinear')
plt.title('Negative Reviews')
_ = plt.axis('off')

# @title Top Positive Reviewers

df[df['Sentiment'] == 'positive'].groupby('Review_by').size().sort_values(ascending=False).head(10).plot(kind='bar')

# @title Sentiment

from matplotlib import pyplot as plt
import seaborn as sns
df.groupby('Sentiment').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

# @title Sentiment over Time
df.groupby(['Time', 'Sentiment']).size().unstack().plot(kind='line', figsize=(10, 6))

df['Sentiment'] = df['Sentiment'].replace('neutral', 1)
df['Sentiment'] = df['Sentiment'].replace('negative',0 )
df['Sentiment'] = df['Sentiment'].replace('positive', 2)

## Get the Independent Features
X = df.drop('Sentiment', axis=1)

y= df['Sentiment']

X.shape

y.shape

"""## Data Pre-Processing"""

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import pandas as pd
import re
from bs4 import BeautifulSoup

"""### Removing Hashtags"""

# Function to clean text data
def clean_text(text):
    if pd.isnull(text):  # Check if text is NaN
        return ''
    text = BeautifulSoup(str(text), 'html.parser').get_text()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    return text

# Apply cleaning and language processing to the 'Review' column
df['Review'] = df['Review'].apply(clean_text)
df['URL'] = df['URL'].apply(clean_text)
df['Time'] = df['Time'].apply(clean_text)
df['Title'] = df['Title'].apply(clean_text)

"""### Tokenization"""

import nltk
from nltk import word_tokenize
nltk.download('punkt')

corpus= []
# Function to clean and tokenize text data
def tokenize_text(text):
    tokens = word_tokenize(text)
    user_review = ' '.join(tokens)
    return tokens

# Assuming 'df' is your DataFrame containing 'Review' and 'Title' columns
df['review'] = df['Review'] + df['Title']

# Tokenize the 'review' column
df['review_tokens'] = df['review'].apply(tokenize_text)

"""### Lemmatization"""

import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

# Function for language processing (lemmatization)
def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    words = text.split()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)


# Lemmatize the 'review' column
df['review'] = df['review'].apply(lemmatize_text)

# Create a corpus
corpus = df['review'].tolist()

# Print the first few elements of the corpus to verify
print(corpus[:5])

"""### Stop Words"""

nltk.download('stopwords')

# Function to remove stopwords
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))  # or choose the appropriate language
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

df['review'] = df['review'].apply(remove_stopwords)

# Save the preprocessed data to a new Excel file
df.to_excel('preprocessed_dataset.xlsx', index=False)

for i in range(10):
    print(df['review'][i+1])

#corpus

df.head()

"""## Training Model"""

#!pip install tensorflow

import tensorflow as tf

tf.__version__

from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense

corpus[1]

import numpy as np
c= np.array(corpus)
c.shape

"""## One Hot Encoding"""

### Vocabulary size
voc_size=5000

onehot_repr= [one_hot(words,voc_size) for words in corpus]
onehot_repr

corpus[1]

onehot_repr[1]

"""## Using Word2Vec"""

sent_length= 20
embedded_docs= pad_sequences(onehot_repr,padding='post',maxlen= sent_length)
print(embedded_docs)

embedded_docs[1]

len(embedded_docs),y.shape

final_corpus = df['review'].astype(str).tolist()
df_final= pd.DataFrame()
df_final['review']= final_corpus
df_final['Sentiment']= df['Sentiment'].values
df_final.head()

x= df_final['review']
y= df_final['Sentiment']
x[0]

from collections import Counter
Counter(y)

"""## Dividing Data into training and testing"""

import numpy as np
X_final=np.array(embedded_docs)
y_final=np.array(y)

X_final.shape,y_final.shape

from sklearn.model_selection import train_test_split
# Define the sizes for each set
train_size = 0.7
val_size = 0.15
test_size = 0.15

# Split the data into training and the rest
X_train, X_temp, y_train, y_temp = train_test_split(X_final, y_final, test_size=1-train_size, random_state=42)
# Split the remaining data into validation and testing sets
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=test_size/(test_size + val_size), random_state=42)

print("Training set size:", len(X_train))
print("Validation set size:", len(X_val))
print("Testing set size:", len(X_test))

X_train

"""## **Using LSTM - Deep Learning**"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

embedding_vector_features = 40
model = Sequential()
model.add(Embedding(voc_size, embedding_vector_features, input_length=sent_length))
model.add(Dropout(0.3))
model.add(LSTM(100))
model.add(Dense(3, activation='softmax'))  # 3 classes:
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())

### Finally Training
model.fit(X_train,y_train,validation_data=(X_val,y_val),epochs=10,batch_size=64)

y_pred=model.predict(X_test)

y_pred[1]

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score

# Create a label encoder
label_encoder = LabelEncoder()

# Fit the encoder on the class labels
label_encoder.fit(y_test)

# Transform the class labels
y_test_encoded = label_encoder.transform(y_test)

# Make predictions and convert them to class labels
y_pred_labels = np.argmax(y_pred, axis=1)

# Compute the confusion matrix and accuracy
conf_matrix = confusion_matrix(y_test_encoded, y_pred_labels)
accuracy = accuracy_score(y_test_encoded, y_pred_labels)
print("Confusion Matrix:")
print(conf_matrix)
print("Accuracy:", accuracy)

from sklearn.metrics import precision_score, recall_score, f1_score
precision = precision_score(y_test_encoded, y_pred_labels, average='weighted')

# Calculate recall
recall = recall_score(y_test_encoded, y_pred_labels, average='weighted')
# Calculate F1-score
f1 = f1_score(y_test_encoded, y_pred_labels, average='weighted')
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    classes = classes[unique_labels(y_true, y_pred)]
    print('Confusion matrix')

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # Show all ticks
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # Label ticks with the respective list entries
           xticklabels=['Predicted Negative', 'Predicted Neutral', 'Predicted Positive'],
           yticklabels=['Actual Negative', 'Actual Neutral', 'Actual Positive'],
           title=title)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax

# Plot non-normalized confusion matrix
plot_confusion_matrix(y_test, y_pred_labels, classes=np.array([-1, 0, 1]),
                      title='Confusion matrix')


plt.show()

"""## **Using Naive Bayes**"""

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Initialize the Naive Bayes classifier
nb_classifier = MultinomialNB()

# Train the classifier on the training data
nb_classifier.fit(X_train, y_train)

"""## Model Evaluation"""

# Predictions on the validation set
val_predictions = nb_classifier.predict(X_val)

# Calculate accuracy on the validation set
val_accuracy = accuracy_score(y_val, val_predictions)
print("Validation set accuracy:", val_accuracy)

# Predictions on the testing set
test_predictions = nb_classifier.predict(X_test)


# Calculate accuracy on the testing set
test_accuracy = accuracy_score(y_test_encoded, test_predictions)
print("Testing set accuracy:", test_accuracy)

# Compute the confusion matrix and accuracy
conf_matrix = confusion_matrix(y_test,test_predictions)
accuracy = accuracy_score(y_test, test_predictions)
print("Confusion Matrix:")
print(conf_matrix)

from sklearn.metrics import precision_score, recall_score, f1_score
precision = precision_score(y_test_encoded,test_predictions, average='weighted')

# Calculate recall
recall = recall_score(y_test_encoded, test_predictions, average='weighted')
# Calculate F1-score
f1 = f1_score(y_test_encoded,test_predictions, average='weighted')
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

# Plot non-normalized confusion matrix
plot_confusion_matrix(y_test,test_predictions , classes=np.array([-1, 0, 1]),
                      title='Confusion matrix')

plt.show()

"""# Bidirectional LSTM Model"""

from tensorflow.keras.layers import Bidirectional

voc_size, embedding_vector_features

model1= Sequential()
model1.add(Embedding(voc_size, embedding_vector_features,input_length= sent_length))
model1.add(Bidirectional(LSTM(100)))
model1.add(Dense(3,activation= 'softmax'))
model1.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model1.summary())

model1.fit(X_train,y_train, validation_data= (X_test,y_test),epochs= 10,batch_size=32)

y_pred1= model1.predict(X_test)

y_pred1= np.where(y_pred1>= 0.5,1,0)

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score

# Make predictions and convert them to class labels
y_pred_label = np.argmax(y_pred1, axis=1)

# Compute the confusion matrix and accuracy
conf_matrix = confusion_matrix(y_test_encoded, y_pred_label)
accuracy = accuracy_score(y_test_encoded, y_pred_label)
print("Confusion Matrix:")
print(conf_matrix)
print("Accuracy:", accuracy)

from sklearn.metrics import precision_score, recall_score, f1_score
precision = precision_score(y_test_encoded, y_pred_label, average='weighted')

# Calculate recall
recall = recall_score(y_test_encoded, y_pred_label, average='weighted')
# Calculate F1-score
f1 = f1_score(y_test_encoded, y_pred_label, average='weighted')
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

import seaborn as sns
from sklearn.utils.multiclass import unique_labels

# Plot non-normalized confusion matrix
plot_confusion_matrix(y_test, y_pred_label, classes=np.array([-1, 0, 1]),
                      title='Confusion matrix')

plt.show()

"""## RNN"""

!pip install tensorflow-addons

import tensorflow as tf
from tensorflow.keras import layers
import tensorflow as tf
from tensorflow.keras.optimizers import SGD


model3= Sequential()
model3.add(Embedding(voc_size, embedding_vector_features,input_length= sent_length))
# Add a SimpleRNN layer\
model3.add(layers.SimpleRNN(units=64))
model3.add(Dense(units=3, activation='softmax'))

model3.compile(loss='sparse_categorical_crossentropy', optimizer='SGD', metrics=['accuracy'])
print(model3.summary())

model3.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_val, y_val))

y_pred3= model3.predict(X_test)

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score

# Make predictions and convert them to class labels
y_pred_label3 = np.argmax(y_pred3, axis=1)

# Compute the confusion matrix and accuracy
conf_matrix3 = confusion_matrix(y_test_encoded, y_pred_label3)
accuracy3 = accuracy_score(y_test_encoded, y_pred_label3)
print("Confusion Matrix:")
print(conf_matrix3)
print("Accuracy:", accuracy3)

from sklearn.metrics import classification_report
report= classification_report(y_test, y_pred_label3 )
print(report)

"""# CNN"""

max_length =sent_length
import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, Conv1D, MaxPooling1D, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D,GlobalMaxPooling1D, Flatten, Dense

# Define the Sequential model
model4 = Sequential()

# Add an embedding layer with vocabulary size voc_size and embedding dimension 100
model4.add(Embedding(voc_size, 100, input_length=max_length))

# Add a 1D convolutional layer with 32 filters and kernel size 8, using ReLU activation
model4.add(Conv1D(filters=32, kernel_size=8, activation='relu'))
# Add a global max pooling layer with pool size 2
model4.add(GlobalMaxPooling1D())

# Flatten the output
model4.add(Flatten())

# Add the output layer with 3 units and softmax activation for multi-class classification
model4.add(Dense(3, activation='softmax'))

# Print the model summary
print(model4.summary())

model4.compile(optimizer= 'adam', loss= 'SparseCategoricalCrossentropy', metrics= 'accuracy')

model4.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))

y_pred4= model4.predict(X_test)

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score

# Make predictions and convert them to class labels
y_pred_label4 = np.argmax(y_pred4, axis=1)

# Compute the confusion matrix and accuracy
conf_matrix4 = confusion_matrix(y_test_encoded, y_pred_label4)
accuracy4 = accuracy_score(y_test_encoded, y_pred_label4)
print("Confusion Matrix:")
print(conf_matrix4)
print("Accuracy:", accuracy4)

from sklearn.metrics import classification_report
report= classification_report(y_test, y_pred_label4 )
print(report)

"""# CNN-LSTM"""

model5= Sequential()
model5.add(Embedding(voc_size, 100, input_length= max_length))
model5.add(Conv1D(filters= 24, kernel_size= 8, activation= 'elu'))
model5.add(LSTM(50))
model5.add(Dense(3,activation='softmax'))
model5.compile(loss= 'sparse_categorical_crossentropy',optimizer='adam',metrics='accuracy')
print(model5.summary())

model5.fit(X_train,y_train,validation_data= (X_val,y_val), epochs= 10,batch_size= 64)

y_pred5= model.predict(X_test)

y_pred_labels5= np.argmax(y_pred5, axis=1)

conf_matrix5= confusion_matrix(y_test_encoded,y_pred_labels5)
print("Confusion matrix:")
print(conf_matrix5)

accuracy5= accuracy_score(y_test_encoded, y_pred_labels5)
print("Accuracy:", accuracy5)

