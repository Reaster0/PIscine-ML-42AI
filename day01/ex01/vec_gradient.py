import numpy as np

def gradient(x, y, theta):
	temp = np.ones((len(x), 1))
	x_prim = np.hstack((temp, np.atleast_2d(x).T))
	return np.divide(np.matmul(x_prim.T, np.subtract(np.matmul(x_prim, theta), y)), len(y))

x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])
# Example 0:
theta1 = np.array([2, 0.7])
print (gradient(x, y, theta1))