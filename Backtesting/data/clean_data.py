import pandas as pd
from io import StringIO

df = pd.read_csv('/Users/jay/Desktop/XRP-price-model/Backtesting/data/cleaned_xrp.csv')


df['<DATE>'] = df['<DATE>'].astype(str)
df['<TIME>'] = df['<TIME>'].astype(str).str.zfill(6)

df['<DATETIME>'] = pd.to_datetime(df['<DATE>'] + df['<TIME>'], format='%Y%m%d%H%M%S')

df = df.drop(columns=['<DATE>','<TIME>'])

output_path = '/Users/jay/Desktop/XRP-price-model/Backtesting/data/cleaned_xrp.csv'
df.to_csv(output_path, index=False)

# print(df.head(1))

