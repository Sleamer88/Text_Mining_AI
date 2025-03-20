import pandas as pd
df = pd.read_csv('vader_data_2.csv')
row_count = sum(1 for row in df['text'])
print(row_count)
