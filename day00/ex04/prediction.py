import numpy as np

def predict_(x, theta):
	new_row = np.ones(len(x), dtype=np.int8)
	result = np.dot(np.hstack((np.transpose([new_row]), np.transpose([x]))), theta)
	return result

x = np.arange(1,6)
theta = np.array ([-3, 1])
print(x)
print(theta)
print(predict_(x, theta))