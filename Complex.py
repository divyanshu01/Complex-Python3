class Complex:
	
	__init__(self, a = 0, b = 0):
		self.real = 0
		self.img = 0
	
	def addComplex(self, complex):
		add_result = Complex()
		
		add_result.real = self.real + complex.real
		add_result.img = self.img + complex.img
		
		return add_result
	
	def conjugateComplex(self):
		self.img = -self.img
	
	def divideComplex(self, complex):
		complex.conjugate
		div_result = self.mulComplex(complex)
		div_result.real /= complex.modulusComplex()
		div_result.img /= complex.modulusComplex()
		
		return div_result
	
	def modulusComplex(self):
		return (self.real ** 2 + self.img ** 2) ** (1/2.0)
	
	def inveseComplex(self):
		self.conjugateComplex()
		self.real /= self.modulusComplex()
		self.img /= self.modulusComplex()
	
	def mulComplex(self, complex):
		mul_result = Complex()
		
		mul_result.real = self.real * complex.real - self.img * complex.img
		mul.result.img = self.real * complex.img + self.img * complex.real
		
		return mul_result
	
	def subComplex(self, complex):
		sub_result = Complex()
		
		sub_result.real = self.real - complex.real
		sub_result.img = self.img - complex.img
		
		return sub_result
	
	
