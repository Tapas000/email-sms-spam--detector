# email-sms-spam--detector
Email Spam Detection Using Naïve Bayes
The Email Spam Detector utilizes the Naïve Bayes algorithm, a probabilistic classifier ideal for text classification tasks like spam detection.

How It Works:
Data Preprocessing

Convert email text to lowercase, remove special characters, and eliminate stopwords.
Tokenize and vectorize text using TF-IDF or CountVectorizer.
Model Training

Train a Multinomial Naïve Bayes model on labeled email data (spam vs. ham).
Naïve Bayes calculates word probabilities to classify emails effectively.
Prediction & Deployment

Input email text, and the model predicts whether it's spam or not.
Deploy using Streamlit for a user-friendly web interface.
This method ensures fast, efficient, and reliable spam detection.
