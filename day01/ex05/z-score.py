import numpy as np

def mean(x):
	assert isinstance(x, np.ndarray), "invalid value for mean"
	result = 0.0
	total = 0
	for arr in x:
		for value in arr:
			total += 1
			result += value
	if total:
		result /= total
	return result

def variance(x):
	assert isinstance(x, np.ndarray), "invalid value for mean"
	one_list = []
	for arr in x:
		for value in arr:
			one_list.append((value - mean(x)) * (value - mean(x)))
	result = 0
	for value in one_list:
		result += value
	return result / (len(one_list))

def std_dev(x):
	assert isinstance(x, np.ndarray), "invalid value for mean"
	return (np.sqrt(variance(x)))

def zscore(x):
	assert isinstance(x, np.ndarray), "invalid value for x"
	x_prim = []
	for i in range(len(x)):
		x_prim.append((x[i] - mean(x)) / std_dev(x))
	return x_prim

print (zscore(np.array([[0], [15], [-9], [7], [12], [3], [-21]])))