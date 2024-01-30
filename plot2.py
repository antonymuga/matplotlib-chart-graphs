import matplotlib.pyplot as my_plt
import numpy as np
import pandas as pd

labels = ['A', 'B', 'C']
values = [1,4,2]

bars = my_plt.bar(labels, values)
# bars[0].set_hatch('/')
# bars[1].set_hatch('*')
# bars[2].set_hatch('-')
patterns = ['/', 'o', '*']
for bar in bars:
	bar.set_hatch(patterns.pop(0))

my_plt.title("This is our First Bar Graph")
my_plt.show()