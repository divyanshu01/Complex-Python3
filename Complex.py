class Complex:
	
	def __init__(self, a = 0, b = 0):
		self.real = a
		self.img = b
	
	def addComplex(self, complex):
		add_result = Complex()
		
		add_result.real = self.real + complex.real
		add_result.img = self.img + complex.img
		
		return add_result
	
	def conjugateComplex(self):
		self.img = -self.img
	
	def divideComplex(self, complex):
		complex.conjugateComplex()
		
		div_result = self.mulComplex(complex)
		div_result.real /= round(complex.modulusComplex() * 1.0, 2)
		div_result.img /= round(complex.modulusComplex() * 1.0, 2)
		
		return div_result
	
	def modulusComplex(self):
		return round(((self.real ** 2 + self.img ** 2) ** (1/2.0)), 2)
	
	def inveseComplex(self):
		self.conjugateComplex()
		self.real /= self.modulusComplex()
		self.img /= self.modulusComplex()
	
	def mulComplex(self, complex):
		mul_result = Complex()
		
		mul_result.real = self.real * complex.real - self.img * complex.img
		mul_result.img = self.real * complex.img + self.img * complex.real
		
		return mul_result
		
	def printComplex(self):
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
		sub_result = Complex()
		
		sub_result.real = self.real - complex.real
		sub_result.img = self.img - complex.img
		
		return sub_result
	
	
