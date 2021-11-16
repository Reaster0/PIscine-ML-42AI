class Matrix(object):
	def __init__(self, *args):
		self.data = []
		assert isinstance(args[0], int) and isinstance(args[0], int) or isinstance(args[0][0], list), "Values input error"
		if isinstance(args[0], int):
			for i in range(args[0]):
				self.data.append([0] * args[1])
			self.shape = (len(self.data), len(self.data[0]))
		elif isinstance(args[0][0], list):
			#print(args)
			for arr in args[0]:
				self.data.append(arr)
				#print(self.data)
			self.shape = (len(self.data), len(self.data[0]))
		
	def __add__(self, other):
		result = []
		for i, rows in enumerate(other.data):
			row = []
			for j, value in enumerate(rows):
				row.append(self.data[i][j] + value)
			result.append(row)
		return Matrix(result)

	def __sub__(self, other):
		result = []
		for i, rows in enumerate(other.data):
			row = []
			for j, value in enumerate(rows):
				row.append(self.data[i][j] - value)
			result.append(row)
		return Matrix(result)
	
	def __truediv__(self, other):
		result = []
		for i, rows in enumerate(other.data):
			row = []
			for j, value in enumerate(rows):
				row.append(self.data[i][j] / value)
			result.append(row)
		return Matrix(result)

	def __mul__(self, other):
		result = []
		for i, rows in enumerate(other.data):
			row = []
			for j, value in enumerate(rows):
				row.append(self.data[i][j] * value)
			result.append(row)
		return Matrix(result)
	
	def __str__(self):
		return self.data
	def __repr__(self):
		return ("shape = " + str(self.shape) + " and data = " + str(self.data))

class Vector(Matrix):# WIP
	values = []
	shapes = []

	def __init__(self, values):
		if isinstance(values, int):
			for i in range(values):
				self.values.append(float(i))
		elif isinstance(values, float) or isinstance(values, list):
			self.values = values
		if type(values[0]) == float:
			self.shapes = [len(values), 1]
		elif type(values[0] == list):
			self.shapes = [1, len(values)]
		else:
		 	raise ValueError

	def __add__(self, other):
		result = []
		assert self.shapes == other.shapes and self.shapes != [1, 1], "the vectors aren't of the same size or it's size 1, 1"
		for idY in range(len(self.values)):
			if type(self.values[idY]) == list:
				result.append([self.values[idY][0] + other.values[idY][0]])
			else:
				result.append(self.values[idY] + other.values[idY])
		return Vector(result)


	def __radd__(self, other):
		result = []
		assert self.shapes == other.shapes and self.shapes != [1, 1], "the vectors aren't of the same size or it's size 1, 1"
		for idY in range(len(self.values)):
			if type(self.values[idY]) == list:
				result.append([other.values[idY][0] + self.values[idY][0]])
			else:
				result.append(other.values[idY] + self.values[idY])
		return Vector(result)

	def __sub__(self, other):
		result = []
		assert self.shapes == other.shapes and self.shapes != [1, 1], "the vectors aren't of the same size or it's size 1, 1"
		for idY in range(len(self.values)):
			if type(self.values[idY]) == list:
				result.append([other.values[idY][0] - self.values[idY][0]])
			else:
				result.append(other.values[idY] - self.values[idY])
		return Vector(result)
	
	def __mul__(self, other):
		result = []
		assert self.shapes == other.shapes and self.shapes != [1, 1], "the vectors aren't of the same size or it's size 1, 1"
		for idY in range(len(self.values)):
			if type(self.values[idY]) == list:
				result.append([self.values[idY][0] * other.values[idY][0]])
			else:
				result.append(self.values[idY] * other.values[idY])
		return Vector(result)
		
	def __truediv__(self, other):
		result = []
		assert self.shapes == other.shapes and self.shapes != [1, 1], "the vectors aren't of the same size or it's size 1, 1" #check zero case
		for idY in range(len(self.values)):
			if type(self.values[idY]) == list:
				result.append([self.values[idY][0] / other.values[idY][0]])
			else:
				result.append(self.values[idY] / other.values[idY])
		return Vector(result)

	def __str__(self):
		return ("values = " + str(self.values) + " shapes = " + str(self.shapes))
	
	def __repr__(self):
		return ("this is a vector = " + str(self.values))

	def dot(self, other):
		result = 0
		assert self.shapes == other.shapes and self.shapes != [1, 1], "the vectors aren't of the same size or it's size 1, 1"
		for idY in range(len(self.values)):
			if type(self.values[idY]) == list:
				result += (self.values[idY][0] * other.values[idY][0])
			else:
				result += (self.values[idY] * other.values[idY])
		return result

	def T(self):
		result = []
		assert self.shapes != [1, 1], "it's size 1, 1"
		for idY in range(len(self.values)):
			if type(self.values[idY]) == list:
				result.append(self.values[idY][0])
			else:
				result.append([self.values[idY]])
		
		return Vector(list(result))

#lol = Matrix(2,4)
lol = Matrix([[1,2,3], [1,2,3]])
lol2 = Matrix([[1,2,3], [1,2,3]])
print (lol.data)
result = lol + lol2
print(result.data)
