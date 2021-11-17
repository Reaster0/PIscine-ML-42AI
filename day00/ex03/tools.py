import numpy as np

def add_intercept(x):
	new_row = np.ones(len(x), dtype=np.int8)
	return np.hstack((np.transpose([new_row]), x))

x = np.arange(1,10).reshape((3, 3))
print (add_intercept(x))