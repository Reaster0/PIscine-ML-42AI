import numpy as np
import matplotlib.pyplot as plt

def predict_(x, theta):
	new_row = np.ones(len(x), dtype=np.int8)
	print(x)
	print(theta)
	result = np.dot(np.hstack((np.transpose([new_row]), np.transpose([x]))), theta)
	return result

def plot(x, y, theta):
	plt.figure(figsize=(4, 3))
	ax = plt.axes()
	ax.scatter(x, y)
	solution = predict_(x, theta)
	ax.plot(x, solution) #x and predict x
	plt.show()

x = np.arange(1,6)
y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
theta1 = np.array([4.5, -0.2])
theta2 = np.array([-1.5, 2])
plot(x, y, theta1)