import json
import csv
file1 = 'merged_training_data.json'
def json_to_csv(file1):
    with open(file1, "r", encoding="utf-8") as f:
        combined_data = json.load(f)
    csv_filename = "vader_data_2.csv"
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["label", "text", "positive", "negative", "neutral", "compound", "vader_label"])
        for key, value in combined_data.items():
            label = value.get("sentiment_label", "")
            text = value.get("text_of_tweet", "")
            csv_writer.writerow([label, text, "", ""])
json_to_csv(file1)