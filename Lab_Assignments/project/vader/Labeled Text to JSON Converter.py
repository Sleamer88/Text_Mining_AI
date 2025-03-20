import json
def convert_text_to_json(text_file_path, json_file_path):
    with open(text_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    data = {}
    index = 1
    for line in lines:
        #__laber__1 and __label__2 can be swapped out with appropriate labels
        if line.startswith('__label__2'):
            sentiment = "positive"
            text = line.replace('__label__2', '').strip()
        elif line.startswith('__label__1'):
            sentiment = "negative"
            text = line.replace('__label__1', '').strip()
        else:
            continue
        data[str(index)] = {
            "sentiment_label": sentiment,
            "text_of_tweet": text
        }
        index += 1
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
text_file_path = input('Input the text file path: ')
json_path = input('Input the json file path: ')
convert_text_to_json(text_file_path, json_path)