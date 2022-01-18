import numpy as np

def simple_predict(x, theta):
	y_hat = []
	for j in range(len(x)):
		temp = theta[0]
		for i in range(1, len(x[j])):
			temp += theta[i] * x[j][i]
		y_hat.append(temp)
	return y_hat


X = np.arange(1,13).reshape((4,3))

theta1 = np.array([[5], [0], [0], [0]])
print(simple_predict(X, theta1))