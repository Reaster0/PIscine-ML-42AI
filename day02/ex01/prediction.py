import numpy as np

def predict_(x, theta):
	x_prim = np.hstack((np.ones((len(x), 1)), x))
	return np.matmul(x_prim, theta)

x = np.arange(1,13).reshape((4,3))
# Example 0:
theta1 = np.array([[5],[ 0],[ 0],[ 0]])
theta2 = np.array([[0], [1], [0], [0]])
print (predict_(x, theta2))