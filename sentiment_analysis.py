from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd
import matplotlib.pyplot as plt
import re
#nltk.download('all')
#nltk.download('vader_lexicon')


sia = SentimentIntensityAnalyzer()
def preprocess_text(text):

    # Tokenize the text
    text = str(text)
    tokens = word_tokenize(text.lower())

    # Remove stop words

    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    # Lemmatize the tokens

    lemmatizer = WordNetLemmatizer()

    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    # Join the tokens back into a string

    processed_text = ' '.join(lemmatized_tokens)

    return processed_text



def get_sentiment_score(comment):

    comment = str(comment)

    return sia.polarity_scores(comment)["compound"]

df = pd.read_csv("real_reddit_comments_2_28_24.csv")

df['Comment'] = df['Comment'].apply(preprocess_text)

comments = df['Comment']
print(comments.head())
sentiment_scores = [get_sentiment_score(comment) for comment in comments]

stock_ticker = "mara"

intensity = SentimentIntensityAnalyzer()


def analyze_sentiment_for_ticker(comments, stock_ticker):
    filtered_comments = [comment for comment in comments if isinstance(comment, str) and stock_ticker in comment]
    sentiment_scores = [intensity.polarity_scores(comment)["compound"] for comment in filtered_comments]
    return sentiment_scores


sentiment_scores_for_ticker = analyze_sentiment_for_ticker(comments, stock_ticker)
print(sentiment_scores_for_ticker)


plt.hist(sentiment_scores_for_ticker, bins=20, edgecolor='black')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.title('Sentiment Analysis for ' + stock_ticker)
plt.show()



plt.hist(sentiment_scores, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.title('Distribution of Sentiment Scores')
plt.show()
