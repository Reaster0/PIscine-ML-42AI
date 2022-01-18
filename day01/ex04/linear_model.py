if __name__ == '__main__':
	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt
	import csv
	from my_linear_regression import MyLinearRegression as MyLR
	from sklearn.metrics import mean_squared_error


	data = pd.read_csv('/Users/reaster/42-Work/PIscine-ML-42AI/day01/ex04/are_blue_pills_magics.csv')
	Xpills = np.array(data['Micrograms']).reshape(-1, 1)
	Yscore = np.array(data['Score']).reshape(-1, 1)

	#plt.scatter(data['Micrograms'], data['Score'])
	#plt.xlabel('Quantity of blue pill (in Micrograms)')
	#plt.ylabel('Space Driving Score')
	linearModel1 = MyLR(np.array([[89.0], [-8]]))
	y_model1 = linearModel1.predict_(Xpills)
	all_model = []
	all_theta1 = []
	for index in range(-14, 0):
		all_model.append(MyLR(np.array([[89.0], [index]])))
		all_theta1.append(index)
	print(all_theta1)
	#print(linearModel1.mse_(Yscore, y_model1)[0])
	#print(mean_squared_error(Yscore, y_model1))
	#plt.figure(1)
	#plt.plot(Xpills, y_model1, 'g+--')
	plt.figure(2)
	plt.ylabel('cost function j(theta0, theta1')
	#for index in range(len(all_model)):
		#print(linearModel1.mse_(Yscore, all_model[index].predict_(Xpills)))
		#plt.scatter(all_theta1[index], linearModel1.mse_(Yscore, all_model[index].predict_(Xpills)))
	all_loss = []
	for index in range(len(all_model)):
		all_loss.append(linearModel1.mse_(Yscore, all_model[index].predict_(Xpills)))
	plt.plot(all_theta1, all_loss)

	# linearModel2 = MyLR(np.array([[89.0], [-6]]))
	# y_model2 = linearModel2.predict_(Xpills)
	# print(linearModel2.mse_(Yscore, y_model2)[0])

	plt.show()