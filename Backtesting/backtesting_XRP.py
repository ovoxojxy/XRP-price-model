import pandas as pd

data = pd.read_csv('/Users/jay/Desktop/XRP-price-model/Backtesting/data/cleaned_xrp.csv')

# df['Date'] = pd.to_datetime(df['Date'])

# df = df.sort_values('Date').reset_index(drop=True)

# for i in range(0, len(df)):
    # df.loc[i, 'Price'] = float(df.loc[i, 'Price'].replace(',', ''))

initial_capital = 115
buy_threshold = -.04
sell_threshold = .06
position = 0
cash = initial_capital
XRP_holdings = 0

for i in range(1, len(data)):
    #calculate percentage change from the previous day
    # pct_change = float(data['Change %'][i][:-1])
    pct_change = (data['<CLOSE>'][i] - data['<OPEN>'][i - 1]) / data['<CLOSE>'][i - 1]

    if position == 0 and pct_change <= buy_threshold:
        #buy XRP
        XRP_holdings = cash / float(data['<CLOSE>'][i])
        cash = 0
        position = 1
        # print(f"Bought XRP on ${data['<DATETIME>'][i]} at ${data['<CLOSE>'][i]:.2f}")

    elif position == 1 and pct_change >= sell_threshold:
        #sell XRP
        cash = XRP_holdings * data['<CLOSE>'][i]
        XRP_holdings = 0
        position = 0
        # print(f"Sold XRP on ${data['<DATETIME>'][i]} at ${data['<CLOSE>'][i]:.2f}")

final_value = cash + XRP_holdings * data['<CLOSE>'].iloc[-1]
# print(f"Final portfolio value: ${final_value:.2f}")


