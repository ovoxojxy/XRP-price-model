import pandas as pd

data = pd.read_csv('')



initial_capital = 115
buy_threshold = -.04
sell_threshold = .06
position = 0
cash = initial_capital
ASSET_holdings = 0

for i in range(1, len(data)):

    pct_change = (data['<CLOSE>'][i] - data['<OPEN>'][i - 1]) / data['<CLOSE>'][i - 1]

    if position == 0 and pct_change <= buy_threshold:

        ASSET_holdings = cash / float(data['<CLOSE>'][i])
        cash = 0
        position = 1
        # print(f"Bought ASSET on ${data['<DATETIME>'][i]} at ${data['<CLOSE>'][i]:.2f}")

    elif position == 1 and pct_change >= sell_threshold:
      
        cash = ASSET_holdings * data['<CLOSE>'][i]
        ASSET_holdings = 0
        position = 0
        # print(f"Sold ASSET on ${data['<DATETIME>'][i]} at ${data['<CLOSE>'][i]:.2f}")

final_value = cash + ASSET_holdings * data['<CLOSE>'].iloc[-1]
# print(f"Final portfolio value: ${final_value:.2f}")


