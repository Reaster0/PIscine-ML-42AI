import numpy as np

class MyLinearRegression():
	def __init__(self, thetas, alpha=0.001, max_iter=1000):
		self.alpha = alpha
		self.max_iter = max_iter
		self.thetas = thetas
	def loss_elem_(y, y_hat):
		result = []
		for index, i in enumerate(y):
			result.append(pow(y_hat[index] - i, 2))
	def mse_(self, y, y_hat):
		result = 0.0
		for index, i in enumerate(y):
			result += pow(y_hat[index] - i, 2)
		return (result / len(y_hat))
	def predict_(self, x):
		new_row = np.ones(len(x), dtype=np.int8)
		result = np.dot(np.hstack((np.transpose([new_row]), x)), self.thetas)
		return result
	def gradient_(self, x, y):
		temp = np.ones((len(x), 1))
		x_prim = np.hstack((temp, x))
		return np.divide(np.matmul(x_prim.T, np.subtract(np.matmul(x_prim, self.thetas), y)), len(y))
	def fit_(self, x, y):
		for i in range(self.max_iter):
			temp = self.gradient_(x, y)
			self.thetas = np.subtract(self.thetas, np.multiply(temp, self.alpha))