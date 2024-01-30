import matplotlib.pyplot as my_plt
import numpy as np
import pandas as pd

gas = pd.read_csv('gas_prices.csv')

my_fig = my_plt.figure(figsize=(8, 6), dpi=120, facecolor='lightgray', edgecolor='blue')
my_plt.plot(gas.Year, gas.USA, 'r.-', label='USA')
my_plt.plot(gas.Year, gas.Canada, 'b.-', label='Canada')
my_plt.title('USA vs Canada Gas Prices')
my_plt.ylabel('Dollars/gallon')
my_plt.legend()
my_plt.xticks(gas.Year[::3].tolist()+[2011])
my_plt.show()