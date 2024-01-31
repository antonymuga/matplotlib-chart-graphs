import matplotlib.pyplot as my_plt
import pandas as pd
import numpy as np

my_plt.style.use('ggplot')

my_data = pd.read_csv('fifa_data.csv')
left_foot = my_data.loc[my_data['Preferred Foot'] == 'Left'].count()[0]
right_foot = my_data.loc[my_data['Preferred Foot'] == 'Right'].count()[0]

labels = ['Left', 'Right']
# colors = ['red', 'green', 'blue']
# my_plt.pie([left_foot, right_foot], labels=labels, colors=colors, autopct='%.1f%%')

my_data.Weight = [int(weight_lbs.strip('lbs')) if type(weight_lbs)==str else weight_lbs for weight_lbs in my_data.Weight]

light_weight = my_data.loc[my_data.Weight < 125].count()[0]
light_medium = my_data.loc[(my_data.Weight >= 125) & (my_data.Weight < 150)].count()[0]
medium_weight = my_data.loc[(my_data.Weight >= 150) & (my_data.Weight < 175)].count()[0]
medium_heavy = my_data[(my_data.Weight >= 175) & (my_data.Weight < 200)].count()[0]
heavy_weight = my_data.loc[my_data.Weight > 200].count()[0]

labels_weight = ['Light Weight','Light Medium','Medium Weight', 'Medium Heavy', 'Heavy']
explode = (.4,.2, 0, 0, .4)
my_plt.pie([light_weight, light_medium, medium_weight, medium_heavy, heavy_weight], labels=labels_weight, autopct='%.1f%%', pctdistance=0.8, explode=explode)
my_plt.show()
