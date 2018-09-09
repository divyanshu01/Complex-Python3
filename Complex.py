class Complex:
	
	def __init__(self, a = 0, b = 0):
	"""
		Parameterized constructor of the class Complex
	"""
		
		self.real = a
		self.img = b
	
	def read_complex(self, number=''):
	"""
		Function to read complex number in any patter given.
		Still work under progress.
	"""
		if number == '':
			raise Exception('No number is provided')
		
		number = number.replace(' ', '')
		
		# Handling unnecessary plus signs
		# Handling needs to be better
		if number[0] == '+':
			number = number[1:]
		split_list = number.split('+')
		if len(split_list) <= 2:
			if len(split_list) == 2:
				if 'i' in split_list[0]:
					self.img = int(split_list[0].replace('i', ''))
				else:
					self.real = int(split_list[0])
			else if len(split_list) == 1:



		else:
			raise Exception('Invalid expression input')

	
	def addComplex(self, complex):
	"""
		Function to add two complex numbers represented by Complex class objects
	"""
		
		add_result = Complex()
		
		add_result.real = self.real + complex.real
		add_result.img = self.img + complex.img
		
		return add_result
	
	def conjugateComplex(self):
	"""
		Conjugates the complex number that is represented by the calling Complex class object
	"""
		
		self.img = -self.img
	
	def divideComplex(self, complex):	
	"""
		Function to divide two complex numbers and return the rounded result represented by a new object
		of the same class
	"""
		
		complex.conjugateComplex()
		
		div_result = self.mulComplex(complex)
		div_result.real /= round(complex.modulusComplex() * 1.0, 2)
		div_result.img /= round(complex.modulusComplex() * 1.0, 2)
		
		return div_result
	
	def modulusComplex(self):
	"""
		Returns the modulus value of the complex number
	"""
		
		return round(((self.real ** 2 + self.img ** 2) ** (1/2.0)), 3)
	
	def inveseComplex(self):
	"""
		Returns the rationalized result of the recirpocal of the given complex number
	"""
		
		self.conjugateComplex()
		self.real /= self.modulusComplex()
		self.img /= self.modulusComplex()
	
	def mulComplex(self, complex):	
	"""
		Function to multiply two complex numbers
	"""
		
		mul_result = Complex()
		
		mul_result.real = self.real * complex.real - self.img * complex.img
		mul_result.img = self.real * complex.img + self.img * complex.real
		
		return mul_result
		
	def printComplex(self):
	"""
		Function to print the complex numbers on the screen
	"""
		
		if self.real == 0:
			if self.img == 0:
				print(0)
			else:
				print(self.img, end = "")
				print('i')
		else:
			if self.img == 0:
				print(self.real)
			elif self.img < 0:
				print(self.real, '-', abs(self.img), end = '')
				print('i')
			else:
				print(self.real, '+', self.img, end = '')
				print('i')
	
	def subComplex(self, complex):
	"""
		Function to return the result of the subtraction of two complex numbers
	"""
		
		sub_result = Complex()
		
		sub_result.real = self.real - complex.real
		sub_result.img = self.img - complex.img
		
		return sub_result
	
	
