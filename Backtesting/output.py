# Define the file path for output
output_file = '/Users/jay/Desktop/XRP-price-model/Backtesting/results/XRP_results.txt'

# Define the results as a multi-line string
results = """Bought XRP on $2024-02-28 20:00:00 at $0.57
Sold XRP on $2024-03-11 17:00:00 at $0.69
Bought XRP on $2024-03-15 05:00:00 at $0.64
Sold XRP on $2024-04-14 01:00:00 at $0.48
Bought XRP on $2024-04-19 04:00:00 at $0.48
Sold XRP on $2024-07-16 17:00:00 at $0.58
Bought XRP on $2024-07-18 05:00:00 at $0.60
Sold XRP on $2024-08-05 17:00:00 at $0.48
Bought XRP on $2024-08-08 02:00:00 at $0.60
Sold XRP on $2024-09-12 15:00:00 at $0.58
Bought XRP on $2024-10-02 23:59:00 at $0.54
Sold XRP on $2024-11-12 10:00:00 at $0.69
Bought XRP on $2024-11-12 12:00:00 at $0.63
Sold XRP on $2024-11-14 19:00:00 at $0.77
Bought XRP on $2024-11-15 01:00:00 at $0.77
Sold XRP on $2024-11-15 03:00:00 at $0.82
Bought XRP on $2024-11-16 18:00:00 at $1.14
Sold XRP on $2024-11-17 15:00:00 at $1.13
Bought XRP on $2024-11-23 18:00:00 at $1.46
Sold XRP on $2024-12-01 21:00:00 at $2.13
Bought XRP on $2024-12-02 10:00:00 at $2.27
Sold XRP on $2024-12-02 16:00:00 at $2.62
Bought XRP on $2024-12-03 09:00:00 at $2.63
Sold XRP on $2024-12-03 13:00:00 at $2.85
Bought XRP on $2024-12-03 15:00:00 at $2.41
Sold XRP on $2024-12-10 21:00:00 at $2.13
Bought XRP on $2024-12-11 03:00:00 at $2.24
Sold XRP on $2024-12-20 15:00:00 at $2.18
Final portfolio value: $244.03"""

# Write the results to a text file
with open(output_file, 'w') as file:
    file.write(results)

print(f"Results successfully written to {output_file}")
