# Fake News Detection System
# Overview
This project implements a Fake News Detection System using machine learning techniques. The system is based on a combination of text features, sentiment analysis, and advanced embeddings to classify news articles as either true or fake.

# Author
Author: Surya Yadav
email: yadavsurya719@email.com
Project Structure
The project is structured as follows:

fake_news_detection.py: Main Python script containing the code for the Fake News Detection System.
True.csv: Dataset containing true news articles.
Fake.csv: Dataset containing fake news articles.
Dependencies
# The project relies on the following libraries and tools:

pandas
scikit-learn
nltk
gensim
vaderSentiment
matplotlib
wordcloud
Ensure that these dependencies are installed before running the script.

Usage
# Download NLTK Resources:

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')


# Option 1: File Upload
Enter the path of the file containing news articles.
# Option 2: Manual Entry
Enter the news article.
View Results:

The script will display the predictions for the provided news articles.
Model Details
The final model utilizes a Voting Classifier combining a Random Forest Classifier and a Multinomial Naive Bayes Classifier. Text features are processed using TF-IDF Vectorizer, and advanced embeddings are generated using Word2Vec. The system also considers text length and sentiment analysis as additional features.

# License
This project is licensed under the MIT License.

