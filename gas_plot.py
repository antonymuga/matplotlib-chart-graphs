import matplotlib.pyplot as my_plt
import numpy as np
import pandas as pd

gas_prices = pd.read_csv('gas_prices.csv')
my_plt.plot(gas_prices.Year, gas_prices.USA, 'r.--', label='USA')
my_plt.plot(gas_prices.Year, gas_prices.Japan, 'g^--', label='Japan')
my_plt.xlabel('Year of Consumption')
my_plt.ylabel('Gas Price')
my_plt.legend()

my_plt.show()