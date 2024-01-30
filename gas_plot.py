import matplotlib.pyplot as my_plt
import numpy as np
import pandas as pd

my_plt.figure(figsize=(8,6))

my_plt.title("Gas price vs. consumption", fontdict={'fontweight':'bold', 'fontsize': 22})

gas_prices = pd.read_csv('gas_prices.csv')
my_plt.plot(gas_prices.Year, gas_prices.USA, 'r.--', label='USA')
my_plt.plot(gas_prices.Year, gas_prices.Japan, 'g^--', label='Japan')
my_plt.plot(gas_prices.Year, gas_prices['South Korea'], 'b.--', label='South Korea')
# countries_to_view = ['Australia', 'USA', 'Japan', 'Canada', 'Japan']
# for country in gas_prices:
# 	if country in countries_to_view:
# 		my_plt.plot(gas_prices['Year'], gas_prices[country], marker='.')

my_plt.xticks(gas_prices.Year[::3].tolist()+[2011])

my_plt.xlabel('Year of Consumption')
my_plt.ylabel('Gas Price')

my_plt.legend(bbox_to_anchor=(1.0, 0.5), loc='upper left')

my_plt.savefig('Gas_price_graph.png', dpi=300)

my_plt.show()