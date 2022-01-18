import numpy as np

def minmax(x):
	x_prim = []
	for i in range(len(x)):
		x_prim.append((x[i] - min(x)) / (max(x) - min(x)))
	return x_prim

X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
print(minmax(X))