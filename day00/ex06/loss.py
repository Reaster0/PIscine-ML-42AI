import numpy as np

def predict_(x, theta):
	new_row = np.ones(len(x), dtype=np.int8)
	result = np.dot(np.hstack((np.transpose([new_row]), x)), theta) #without the transpose
	#result = np.dot(np.hstack((np.transpose([new_row]), np.transpose([x]))), theta)
	return result

def loss_elem_(y, y_hat):
	result = []
	for index, i in enumerate(y):
		result.append(pow(y_hat[index] - i, 2))
	return result

def loss_(y, y_hat):
	result = 0
	for index, i in enumerate(y):
		result += pow(y_hat[index] - i, 2)
	return result / (2 * len(y_hat))

x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])

# print(x1)
# print(theta1)

y_hat1 = predict_(x1, theta1)
y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
print(loss_elem_(y1, y_hat1))

# x2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
# theta2 = np.array([[0.05], [1.], [1.], [1.]])
# y_hat2 = predict_(x2, theta2)
# y_hat2v2 = simple_predict(x2, theta2)
# y2 = np.array([[19.], [42.], [67.], [93.]])
# print(loss_(y2, y_hat2))

# x3 = np.array([0, 15, -9, 7, 12, 3, -21])
# theta3 = np.array([[0.], [1.]])
# y_hat3 = predict_(x3, theta3)
# y3 = np.array([2, 14, -13, 5, 12, 4, -19])
# print (loss_(y3, y_hat3))