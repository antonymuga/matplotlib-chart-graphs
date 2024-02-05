import matplotlib.pyplot as my_plt
import pandas as pd
import numpy as np

my_plt.style.use('default')

my_plt.figure(figsize=(5,8))

my_data = pd.read_csv('fifa_data.csv')
barcelona = my_data.loc[my_data.Club == 'FC Barcelona']['Overall']
madrid = my_data.loc[my_data.Club == 'Real Madrid']['Overall']
revs = my_data.loc[my_data.Club == 'New England Revolution']['Overall']

labels = ['FC Barcelona', 'Real Madrid', 'New England Revolution']

my_plt.title('Comparison of teams')
my_plt.xlabel('Team Name')
my_plt.ylabel('FIFA Overall Rating')
 
boxes = my_plt.boxplot([barcelona, madrid, revs], labels=labels, patch_artist=True, medianprops={'linewidth':2})

for box in boxes['boxes']:
	box.set(color='#4286f4', linewidth=2)
	box.set(facecolor='#e0e0e0')

my_plt.show()