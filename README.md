#Complex-Python3#
###Python library for complex number algebra####
- - - -
This project is an extension to functionality of python 3 so that complex number algebra can be done gracefully with python.

**Complex.py:** The main python file. Just import this module in the main script and create object of Complex class to represent a complex number.

* `addComplex(Complex)`
>This function is called by object of `Complex` class and another object of the same class is passed as argument. It returns another object of `Complex` class with the added result of the two complex numbers.

* `conjugateComplex()`
>This function conjugates the complex number which is represented by the calling `Complex` object.

* `divideComplex(Complex)`
>This function returns a new `Complex` object representing the divided result of the calling `Complex` object and the one passed as an argument. The values are rounded off.

* `modulusComplex()`
>The function returns the modulus value of the complex number represented by the calling `Complex` object. It returns is rounded to upto 2 digits.

* `inverseComplex()`
>This function returns the rationalized result of the inverse of the complex number which is represented by the calling `Complex` object. No new object is returned, the calling object is modified.

* `mulComplex(Complex)`
>This function returns a new `Complex` object representing the product of the calling `Complex` object and the object passed as an argument to the function.

* `subComplex(Complex)`
>This function is called by object of `Complex` class and another object of the same class is passed as argument. It returns another object of `Complex` class with the subtracted result of the two complex numbers.

