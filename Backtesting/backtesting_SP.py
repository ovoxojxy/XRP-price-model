import pandas as pd

data = pd.read_csv('/Users/jay/Desktop/XRP-price-model/Backtesting/data/cleaned_SP500.csv')



initial_capital = 115
buy_threshold = -.01
sell_threshold = .02
position = 0
cash = initial_capital
SP_holdings = 0

for i in range(1, len(data)):

    pct_change = (data['<CLOSE>'][i] - data['<OPEN>'][i - 1]) / data['<CLOSE>'][i - 1]

    if position == 0 and pct_change <= buy_threshold:

        SP_holdings = cash / float(data['<CLOSE>'][i])
        cash = 0
        position = 1
        print(f"Bought SP on ${data['<DATETIME>'][i]} at ${data['<CLOSE>'][i]:.2f}")

    elif position == 1 and pct_change >= sell_threshold:
      
        cash = SP_holdings * data['<CLOSE>'][i]
        SP_holdings = 0
        position = 0
        print(f"Sold SP on ${data['<DATETIME>'][i]} at ${data['<CLOSE>'][i]:.2f}")

final_value = cash + SP_holdings * data['<CLOSE>'].iloc[-1]
print(f"Final portfolio value: ${final_value:.2f}")


