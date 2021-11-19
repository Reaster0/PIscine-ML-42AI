import numpy as np

def mse_(y, y_hat):
	result = 0
	for index, i in enumerate(y):
		result += pow(y_hat[index] - i, 2)
	return result / len(y_hat)

def rmse_(y, y_hat):
	result = 0
	for index, i in enumerate(y):
		result += pow(y_hat[index] - i, 2)
	return np.sqrt(result / len(y_hat))

def mae_(y, y_hat):
	result = 0
	for index, i in enumerate(y):
		result += abs(y_hat[index] - i)
	return result / len(y_hat)

def r2score_(y, y_hat):
	temp = 0
	temp2 = 0
	mean_y = np.mean(y)
	for index, i in enumerate(y):
		temp += pow(y_hat[index] - i, 2)
	for index, i in enumerate(y):
		temp2 += pow(i - mean_y, 2)
	return 1 - temp / temp2

x = np.array([0, 15, -9, 7, 12, 3, -21])
y = np.array([2, 14, -13, 5, 12, 4, -19])
# Mean squared error
## your implementation
print (r2score_(x,y))