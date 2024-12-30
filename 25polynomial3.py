class Polynomial:
	def __init__(self, degree):
		self.__degree = degree
		self.__coefficient = [0] * (self.__degree+1)
		self.__variable = 'x'
	
	def setCoefficient(self, power, coefficient):
		self.__coefficient[power] = coefficient

	def printPolynomail(self):
		i = self.__degree
		while i >= 0:
			if self.__coefficient[i] != 0:
				if i < self.__degree and self.__coefficient[i] > 0:
					print('+ ', end='')
				else:
					print('- ', end='')
				print(abs(self.__coefficient[i]), end='')
				print(self.__variable, end='')
				print('^', end='')
				print(i, end=' ')
				# print('+' if self.__coefficient[i-1] > 0 else '', end=' ')
			i = i-1
		print()

	def value(self, x):
		val = 0
		i = self.__degree
		while i >= 0:
			val = val + self.__coefficient[i] * pow(x, i)
			i = i-1
		return val

def main():
	e = Polynomial(3)
	e.setCoefficient(3, -2)
	e.setCoefficient(2, 5)
	e.setCoefficient(0, -1)
	e.printPolynomail()
	print(e.value(1))
	print(e.value(5))
	print(e.value(-2))

main()
