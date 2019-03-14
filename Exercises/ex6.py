'''
    Generate and plot this dataset (XOR)
    Recall:
    0 XOR 0 = 0
    0 XOR 1 = 1
    1 XOR 0 = 1
    1 XOR 1 = 0
'''


import matplotlib.pyplot as plt 
import numpy as np 


# set color of each point by checking its x & y value
def setColor(x,y):
    if (x < 0 and y < 0) or (x > 0 and y > 0):
        return 'blue'
    else:
        return 'red'


#uniform distribution x and y
x = np.random.uniform(-1.0,1.0,3000)
y = np.random.uniform(-1.0,1.0,3000)

colors = list(map(setColor, x, y))

plt.scatter(x, y, c=colors, marker = 'o', alpha=0.8,edgecolor='k')
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.show()