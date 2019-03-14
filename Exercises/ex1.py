'''
A = [[0.3, 0.6, 0.1], [0.5, 0.2, 0.3], [0.4, 0.1, 0.5]]
v = [1 / 3, 1 / 3, 1 / 3]
You can also initialize v to be random positive numbers just needs to sum to 1
Do this loop
do 25 times:
    v' = vA
    v = v'
By the 25the step you've calculated original v times A^25
On each step, plot the Euclidean distance between |v' - v| as a function of iteration
You should notice that it converges to 0
As a quiz, this about what we've just found (in terms of linear algebra)
'''

import numpy as np 
import matplotlib.pyplot as plt 

A = np.array([[0.3,0.6,0.1],[0.5,0.2,0.3],[0.4,0.1,0.5]])

V = np.array([0.33, 0.33, 0.33])

y = np.array([])

for x in range(0,25):
	v_prime = np.dot(V,A)
	y = np.append(y,np.linalg.norm(v_prime - V))
	V = v_prime

plt.plot(y)
plt.show()


'''
    If |v' - v| = 0, then v' = v = vA
    We've found the eigenvector for A for which the corresponding eigenvalue is 1!
'''

print('The eigenvector is',V)