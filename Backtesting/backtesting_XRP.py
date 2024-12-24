import pandas as pd

data = pd.read_csv('/Users/jay/Desktop/XRP-price-model/Backtesting/data/cleaned_xrp.csv')

initial_capital = 115
buy_threshold = -.04
sell_threshold = .06
position = 0
cash = initial_capital
XRP_holdings = 0
entry_price = 0

trade_log = []

for i in range(1, len(data)):
    current_price = float(data['<CLOSE>'][i])
    datetime = data['<DATETIME>'][i]

    if position == 0:
        #
        pct_change = (data['<CLOSE>'][i] - data['<OPEN>'][i - 1]) / data['<CLOSE>'][i - 1]
        if pct_change <= buy_threshold:
            #
            XRP_holdings = cash / current_price
            cash = 0
            position = 1
            entry_price = current_price
            trade_log.append((datetime, 'BUY', current_price, XRP_holdings))
            print(f"Bought XRP on {datetime} at ${current_price:.2f}")
    elif position == 1:
        #
        pct_change_from_entry = (current_price - entry_price) / entry_price
        if pct_change_from_entry >= sell_threshold:
            #
            cash = XRP_holdings * current_price
            XRP_holdings = 0
            position = 0
            trade_log.append((datetime, "SELL", current_price, cash))
            print(f"Sold XRP on {datetime} at ${current_price:.2f} | Gain: {pct_change_from_entry:.2%}")
        elif pct_change_from_entry <= buy_threshold:
            #
            cash = XRP_holdings * current_price
            XRP_holdings = 0
            position = 0
            trade_log.append((datetime, 'STOP LOSS SELL', current_price, cash))
            print(f"Stop Loss Triggered on {datetime} at ${current_price:.2f} | Loss: {pct_change_from_entry:.2%}")

final_value = cash + (XRP_holdings * data['<CLOSE>'].iloc[-1])
print(f'Final portfolio valie: ${final_value:.2f}')

trade_log_df = pd.DataFrame(trade_log, columns=['Datetime', 'Action', 'Price', 'Amount'])
output_file = '/Users/jay/Desktop/XRP-price-model/Backtesting/results/XRPtrade_log.csv'

# Save DataFrame as CSV
trade_log_df.to_csv(output_file, index=False)




























#     #calculate percentage change from the previous day
#     pct_change = (data['<CLOSE>'][i] - data['<OPEN>'][i - 1]) / data['<CLOSE>'][i - 1]

#     if position == 0 and pct_change <= buy_threshold:
#         #buy XRP
#         XRP_holdings = cash / float(data['<CLOSE>'][i])
#         cash = 0
#         position = 1
#         print(f"Bought XRP on ${data['<DATETIME>'][i]} at ${data['<CLOSE>'][i]:.2f}")

#     elif position == 1 and pct_change >= sell_threshold:
#         #sell XRP
#         cash = XRP_holdings * data['<CLOSE>'][i]
#         XRP_holdings = 0
#         position = 0
#         print(f"Sold XRP on ${data['<DATETIME>'][i]} at ${data['<CLOSE>'][i]:.2f}")

# final_value = cash + XRP_holdings * data['<CLOSE>'].iloc[-1]
# print(f"Final portfolio value: ${final_value:.2f}")


