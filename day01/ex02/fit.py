import numpy as np

def predict_(x, theta):
	new_row = np.ones(len(x), dtype=np.int8)
	result = np.dot(np.hstack((np.transpose([new_row]), x)), theta)
	return result

def gradient(x, y, theta):
	temp = np.ones((len(x), 1))
	x_prim = np.hstack((temp, x))
	return np.divide(np.matmul(x_prim.T, np.subtract(np.matmul(x_prim, theta), y)), len(y))

def fit_(x, y , theta, alpha, max_iter):
	for i in range(max_iter):
		temp = gradient(x, y, theta)
		theta = np.subtract(theta, np.multiply(temp, alpha))
	return theta

x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
theta = np.array([[1], [1]])
# Example 0:
theta1 = fit_(x, y, theta, alpha=5e-6, max_iter=15000)

print (theta1)
print (predict_(x, theta1))