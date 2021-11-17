import numpy as np

def simple_predict(x, theta):
	result = []
	for i in x:
		result.append(theta[0] + theta[1] * i)
	return result
x = np.arange(1,6)
print(simple_predict(x, [-3, 1]))