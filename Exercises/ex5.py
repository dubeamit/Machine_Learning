'''
    Write a function that tests whether or not a matrix is symmetric, i.e.
    def is_symmetric(matrix):
    .....
    Try both ways: the "manual way" (i.e. by using the definition) and by making use of Numpy functions
'''

import numpy as np 


def is_symmetric(matrix):
	return np.array_equal(matrix, matrix.transpose())

a = np.array([[1, 2], [3, 4]])
b = np.array([[1, 0], [0, 1]])

print('Is matrix a symmetric? {}'.format(is_symmetric(a)))
print('Is matrix b symmetric? {}'.format(is_symmetric(b)))