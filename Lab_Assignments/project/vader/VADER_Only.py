import pandas as pd
import nltk
from nltk.sentiment import vader
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nlp = spacy.load('en_core_web_sm')
vader_model = SentimentIntensityAnalyzer()
df = pd.read_csv("vader_data_2.csv")
for row in df.itertuples():
    index = row[0]
    sent = row[2]
    score = vader_model.polarity_scores(sent)
    print("Row {} has score {}".format(index, score))
    positive_score = score['pos']
    negative_score = score['neg']
    neutral_score = score['neu']
    compound_score = score['compound']
    if positive_score > negative_score:
        sentiment = "positive"
    elif negative_score > positive_score:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    df.at[index,"positive"] = positive_score
    df.at[index,"negative"] = negative_score
    df.at[index,"neutral"] = neutral_score
    df.at[index,"compound"] = compound_score
    df.at[index,"vader_label"] = sentiment
df.to_csv("vader_data_2.csv", index=False)