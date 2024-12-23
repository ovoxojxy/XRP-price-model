import pandas as pd

df = pd.read_csv('data_path')

df['Date'] = pd.to_datetime(df['Date'])

df = df.sort_values('Date').reset_index(drop=True)

for i in range(0, len(df)):
    df.loc[i, 'Price'] = float(df.loc[i, 'Price'].replace(',', ''))

initial_capital = 115
buy_threshold = -.04
sell_threshold = .06
position = 0
cash = initial_capital
ASSET_holdings = 0

for i in range(1, len(df)):
    #calculate percentage change from the previous day
    pct_change = float(df['Change %'][i][:-1])

    if position == 0 and pct_change <= buy_threshold:
        #buy ASSET
        ASSET_holdings = cash / float(df['Price'][i])
        cash = 0
        position = 1
        print(f"Bought ASSET on ${df['Date'][i]} at ${df['Price'][i]:.2f}")

    elif position == 1 and pct_change >= sell_threshold:
        #sell ASSET
        cash = ASSET_holdings * df['Price'][i]
        ASSET_holdings = 0
        position = 0
        print(f"Sold ASSET on ${df['Date'][i]} at ${df['Price'][i]:.2f}")

final_value = cash + ASSET_holdings * df['Price'].iloc[-1]
print(f"Final portfolio value: ${final_value:.2f}")
