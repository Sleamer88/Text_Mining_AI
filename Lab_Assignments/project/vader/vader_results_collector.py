import pandas as pd
def ClassificationReportGenerator(csv_file):
    df = pd.read_csv(csv_file)
    TruePositive = 0
    FalsePositive = 0
    TrueNegative = 0
    FalseNegative = 0
    FalseNeutral = 0
    for sent in df.itertuples():
        index = sent[0]
        if sent[1] == "positive" and sent[7]=="positive":
            TruePositive+=1
        if sent[1] == "negative" and sent[7]=="positive":
            FalsePositive+=1
        if sent[1] == "negative" and sent[7]=="negative":
            TrueNegative+=1
        if sent[1] == "positive" and sent[7]=="negative":
            FalseNegative+=1
        if sent[1] == "neutral":
            FalseNeutral+=1
        print("iterating row: {}".format(index))
    AccuracyScore = (TruePositive+TrueNegative)/(TruePositive+FalsePositive+TrueNegative+FalseNegative+FalseNeutral)
    PrecisionScore = (TruePositive)/(TruePositive+FalsePositive)
    RecallScore = (TruePositive)/(TruePositive+FalseNegative)
    F1 = (2*PrecisionScore*RecallScore)/(PrecisionScore+RecallScore)
    ClassificationReport = f"TP: {TruePositive}, FP: {FalsePositive}, TN: {TrueNegative}, FN: {FalseNegative},FNeu: {FalseNeutral}, Accuracy: {AccuracyScore}, Precision: {PrecisionScore}, Recall: {RecallScore}, F1: {F1}"
    open('results_2.txt', 'w').write(ClassificationReport)
ClassificationReportGenerator('vader_data_2.csv')