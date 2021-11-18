import numpy as np
import matplotlib.pyplot as plt

def loss_(y, y_hat):
	return np.dot(np.subtract(y_hat, y),np.subtract(y_hat, y)/ (2 * len(y)))

def predict_(x, theta):
	new_row = np.ones(len(x), dtype=np.int8)
	#result = np.dot(np.hstack((np.transpose([new_row]), x)), theta) #without the transpose
	result = np.dot(np.hstack((np.transpose([new_row]), np.transpose([x]))), theta)
	return result

def plot_with_loss(x, y, theta):
	plt.figure(figsize=(4,3))
	ax = plt.axes()
	ax.scatter(x, y)
	solution = predict_(x, theta)
	diff = loss_(y, solution)
	ax.plot(x, solution)
	for index, value in enumerate(y):
		ax.plot([x[index], x[index]], [value, solution[index]],'.r-' ,linestyle='--')
	ax.set_title("% of loss : " + str(diff))
	plt.show()


x = np.arange(1,6)
y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])

theta1= np.array([18,-1])
plot_with_loss(x, y, theta1)