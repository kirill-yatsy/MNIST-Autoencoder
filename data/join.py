import pandas as pd
import glob
import os
 

months = []

 
for file in glob.glob(f'{os.getcwd()}/data/csv/*.csv'):
    months.append(pd.read_csv(file, names=[
        'open_time',
        'open',
        'high',
        'low',
        'close',
        'volume',
        'close_time',
        'quote_volume',
        'count',
        'taker_buy_volume',
        'taker_buy_quote_volume',
        'ignore'

    ], header=None))

df = pd.concat(months, axis=0, ignore_index=True)

df.to_csv(f'{os.getcwd()}/data/ethusdt.csv', index=False)
