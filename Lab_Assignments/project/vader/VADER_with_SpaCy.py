import pandas as pd
import nltk
from nltk.sentiment import vader
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nlp = spacy.load('en_core_web_sm')
vader_model = SentimentIntensityAnalyzer()
def run_vader(textual_unit, lemmatize=False, parts_of_speech_to_consider=None,):
    doc = nlp(textual_unit)
    input_to_vader = []
    for sent in doc.sents:
        for token in sent:
            to_add = token.text
            if lemmatize:
                to_add = token.lemma_
                if to_add == '-PRON-':
                    to_add = token.text
            if parts_of_speech_to_consider:
                if token.pos_ in parts_of_speech_to_consider:
                    input_to_vader.append(to_add)
            else:
                input_to_vader.append(to_add)
    scores = vader_model.polarity_scores(' '.join(input_to_vader))
    return scores
df = pd.read_csv("vader_data_2.csv")
for row in df.itertuples():
    index = row[0]
    sent = row[2]
    score = run_vader(sent, lemmatize=True, parts_of_speech_to_consider=None)
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