import numpy as np

class TinyStastistician(object):

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
	
	def median(x):
		assert isinstance(x, np.ndarray), "invalid value for mean"
		one_list = []
		for arr in x:
			for value in arr:
				one_list.append(value)
		one_list.sort()
		if len(one_list) % 2:
			return one_list[int(len(one_list) / 2)]
		return (one_list[int(len(one_list) / 2)] + one_list[int(len(one_list) / 2)] - 1) / 2

	def quartile(x):
		assert isinstance(x, np.ndarray), "invalid value for mean"
		one_list = []
		for arr in x:
			for value in arr:
				one_list.append(value)
		one_list.sort()
		first_qrounded = int((len(one_list) + 1) / 4)
		third_qrounded = int(3 * (len(one_list) + 1) / 4)
		if len(one_list) % 2:
			return (one_list[first_qrounded - 1] + one_list[first_qrounded]) / 2, (one_list[third_qrounded - 1] + one_list[third_qrounded]) / 2 #i'm probably wrong here
		return (one_list[first_qrounded - 1] + one_list[first_qrounded]) / 2, (one_list[third_qrounded - 1] + one_list[third_qrounded]) / 2

	def percentile(x, p):
		assert isinstance(x, np.ndarray), "invalid value for mean"
		one_list = []
		for arr in x:
			for value in arr:
				one_list.append(value)
		one_list.sort()
		return one_list[int((p * len(one_list)) / 100)]

	def var(x):
		assert isinstance(x, np.ndarray), "invalid value for mean"
		one_list = []
		for arr in x:
			for value in arr:
				one_list.append((value - TinyStastistician.mean(x)) * (value - TinyStastistician.mean(x)))
		result = 0
		for value in one_list:
			result += value
		print(len(one_list))
		return result / (len(one_list) - 1)
	
	def std(x):
		assert isinstance(x, np.ndarray), "invalid value for mean"
		return (np.sqrt(TinyStastistician.var(x)))

lol = np.array([[1, 42, 300 , 10, 59]])
print (TinyStastistician.std(lol))