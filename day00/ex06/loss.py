import numpy as np

def predict_(x, theta):
	new_row = np.ones(len(x), dtype=np.int8)
	result = np.dot(np.hstack((np.transpose([new_row]), np.transpose([x]))), theta)
	#result = np.dot(np.hstack((np.transpose([new_row]), x)), theta) #without the transpose
	return result

def loss_elem_(y, y_hat):
	result = []
	print(y_hat)
	for where in range(len(y_hat)):
		for index, i in enumerate(y):
			temp = 0
			#print(i,y_hat[index])
			# if index == 0:
			# 	continue
			temp += (np.square(y_hat[index] - i))
		result.append(temp)
		sum = where
		while (sum):
			sum -= 1
			result[where] += result[sum]
	return result

def loss_(y, y_hat):
	sup_result = 0.0
	result = []
	print(y_hat)
	for where in range(len(y_hat)):
		for index, i in enumerate(y):
			temp = 0
			#print(i,y_hat[index])
			# if index == 0:
			# 	continue
			temp += (np.square(y_hat[index] - i))
		result.append(temp / (2 * len(y_hat)))
		sum = where
		while (sum):
			sum -= 1
			sup_result += result[sum]
	return sup_result

x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])

# print(x1)
# print(theta1)

#y_hat1 = predict_(x1, theta1)
y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
# print(y1)
# print ("--------------")
# print(y_hat1)
#print(loss_elem_(y1, y_hat1))


x3 = np.array([0, 15, -9, 7, 12, 3, -21])
theta3 = np.array([[0.], [1.]])
y_hat3 = predict_(x3, theta3)
y3 = np.array([2, 14, -13, 5, 12, 4, -19])
loss_(y3, y_hat3)