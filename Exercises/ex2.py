'''
    Demonstrate the central limit theorem (CLT)
    Recall:
    If Y = X1 + X2 + X3 + ... + XN
    where X are IID (independent, identically distributed)
    Then as N -> infinity, Y -> Gaussian distribution
    Use the uniform distribution as your base for X
    Use N = 1000 (or higher if you want)
    Then draw 1000 Y's (or more if you want)
    Plot histogram of Y's -> should be a "bell curve"
    Bonus: find the expected mean and variance of Y
'''


import numpy as np
import matplotlib.pyplot as plt 

x = np.random.rand(1000,2000) + 1
y = np.sum(x, axis=0)       #1x2000

print('mean of Gaussian Distribution: {0}'.format(y.mean()))
print('variance of Gaussian Distribution: {0}'.format(y.var()))
print('standard deviation of Gaussian Distribution: {0}'.format(y.std()))

plt.hist(y,bins=100)
plt.ylabel('number of Y\'s in a bin')
plt.xlabel('sum of X1 to XN')
plt.show()