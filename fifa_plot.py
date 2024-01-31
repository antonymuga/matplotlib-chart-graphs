import matplotlib.pyplot as my_plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

# bins = [0,10,20,30,40,50,60,70,80,90,100]
my_plt.hist(fifa.Overall, bins=4)
my_plt.xlabel('Skill Level', color='red')
my_plt.ylabel('Number of players',color='green')
my_plt.title('Distribution of Players Skills in FIFA 2018')
my_plt.show()