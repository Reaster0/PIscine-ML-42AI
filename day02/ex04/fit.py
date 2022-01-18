import numpy as np

def predict_(x, theta):
	x_prim = np.hstack((np.ones((len(x), 1)), x))
	return np.matmul(x_prim, theta)

def gradient(x, y, theta):
	x_prim = np.hstack((np.ones((len(x), 1)), x))
	return np.matmul(x_prim.T, np.subtract(np.matmul(x_prim, theta), y)) / len(x)

def fit_(x, y, theta, alpha, max_iter):
	while max_iter:
		theta = theta - alpha * gradient(x, y, theta)
		max_iter = max_iter - 1
	return theta

x = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
theta = np.array([[42.], [1.], [1.], [1.]])
# Example 0:
print(fit_(x, y, theta, alpha = 0.0005, max_iter=42000))

print (predict_(x, fit_(x, y, theta, alpha = 0.0005, max_iter=42000)))