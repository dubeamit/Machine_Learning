'''
    Load in the MNIST dataset, and plot the mean (average) image for each digit class (0....9)
    Recall: mean = sum / number of elements
'''

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv('train.csv')

for i in range(10):
	# get the rows that has class i picture
	class_i = df.loc[df['label'] == i]
	print(class_i.head())

	# delete 'label' column
	no_label_class = class_i.drop('label',axis=1)

	# calculate mean of each column
	class_i_img = no_label_class.mean(axis=0)

	#plot
	plt.imshow(class_i_img.values.reshape(28,28),cmap='gray')
	plt.show()