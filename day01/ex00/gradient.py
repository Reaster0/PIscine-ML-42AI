import numpy as np

def simple_gradient(x, y, theta):
	nabla = []
	temp = 0
	for index, value in enumerate(y):
		predict = theta[0] + theta[1] * x[index]
		temp += predict - value
	nabla.append(temp / len(y))
	temp = 0
	for index, value in enumerate(y):
		predict = theta[0] + theta[1] * x[index]
		temp += (predict - value) * x[index]
	nabla.append(temp / len(y))
	return nabla

x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])
# Example 0:
theta1 = np.array([2, 0.7])
print (simple_gradient(x, y, theta1))