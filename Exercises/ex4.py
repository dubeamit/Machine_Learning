'''
    Continue to work with the MNIST dataset
    Common C programming exercise (with for loops and array indexing)
    Write a function that flips an image 90 degrees clockwise
    Try both the "for loop method" and by making use of Numpy functions
'''

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv('train.csv')

print(df.shape)

imgarray = df.iloc[0,1:].values.reshape(28,28)

rotate_img = np.rot90(imgarray,1)

plt.subplot(1,2,1)
plt.imshow(imgarray, cmap='viridis')

plt.subplot(1,2,2)
plt.imshow(rotate_img, cmap='gray')
plt.show()