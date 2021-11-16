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
		result = 0.0
		one_list = []
		for arr in x:
			for value in arr:
				one_list.append(value)
		one_list.sort()
		print(one_list)
		if len(one_list) % 2:
			return one_list[int(len(one_list) / 2)]
		return (one_list[int(len(one_list) / 2)] + one_list[int(len(one_list) / 2)] - 1) / 2


lol = np.array([[1, 2, 3], [6, 5, 4]])
print (TinyStastistician.median(lol))