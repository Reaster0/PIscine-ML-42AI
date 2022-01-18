import numpy as np

def loss_(y, y_hat):
	temp = np.subtract(y_hat, y)
	return np.dot(temp, temp) / (2 * len(y))

X = np.array([0,15,-9,7,12,3,-21])
Y = np.array([2,14,-13,5,12,4,-19])
# Example 0:
print(loss_(X, Y))