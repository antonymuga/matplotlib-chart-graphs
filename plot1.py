import matplotlib.pyplot as my_plt
import numpy as np
import pandas as pd

# Basic graph

x_cords = [1, 2, 3, 4, 5]
y_cords = [2, 4, 6, 8, 10]

#my_plt.plot(x_cords, y_cords, label='2x', color='green', linewidth='1', linestyle='--', marker='.', markersize=15) # label works with my_plt.legend()

# shorthand of the above commented line
# fmt = '[color][marker][line]'

# example below
my_plt.plot(x_cords, y_cords, 'b^--', label='2x')

t1 = np.arange(0,5.5, 0.5)
my_plt.plot(t1, t1**3, 'r.--',label='t1')
my_plt.xlabel('This is the X-label', color='r', fontdict={'fontname': 'Times New Roman', 'fontsize': 20})
my_plt.ylabel('This is the Y-label', color='b', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
my_plt.title('My fifth plot in Matplotlib', color='g')

my_plt.xticks([0,1,2,3,4,5])
my_plt.yticks([0,2,4,6,8,10])

my_plt.legend()
my_plt.show()