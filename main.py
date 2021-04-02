class Fraction:

  #the constructor for the Fraction class
  #n is the numerator
  #d is the denominator
  #The constructor should create a Fraction object that is reduced
	def __init__(self, num, den):
		self.num = num
		self.den = den

  #Returns a string representation of self. This is needed to print Fractions in a list correctly. 
	def __repr__(self):
		return str(self.num) + "/" + str(self.den)
		
  #If f and g are Fractions, then f * g returns a Fraction that is the
  # sum of f and g
  def __mul__(self, other):
    return Fraction(self.num * other.num, self.den * other.den)

    
  #If f is a Fractions, then ~f returns a Fraction that is the
  #reciprocal of f
  def __invert__(self):
    pass

  #If f is a Fractions, then -f returns a Fraction that is the
  # negation of f. 
  def __neg__(self):
    pass

  #If f and g are Fractions, then f + g returns a Fraction that is the
  # sum of f and g
  def __add__(self, other):
    pass


  #If f and g are Fractions, then f - g returns a Fraction that is the
  # difference of f and g
  #You should implement this method without calling the constructor directly.
  def __sub__(self, other):
    pass

  #If f and g are Fractions, then f / g returns a Fraction that is the
  # quotient of f and g
  #You should implement this method without calling the constructor directly.
  def __truediv__(self, other):
    pass

  #Returns true if self < other. False otherwise
  def __lt__(self, other):
    pass

  #Returns the absolute value of self. If f is a Fraction, this is called as abs(f).
  def __abs__(self):
    pass

  ##Returns a string representation of self as a mixed number. For example, 12/5 as a mixed number is "2 2/5".
  def mixed_number(self):
    pass

#After you finish and test all of the methods above, you should modify the __init__ methods so that it can be passed a string
#representation of a fraction, such as "14/102". To do this, modify the definition of __init__ as shown below,

#__init__(self, n, d = None):

#In your code, check to see if d is None. If it is, then n holds the string representation. If d is not None,
#then n and d are integers representing the numerator and denominator respectively.

#Finally, modify your code so that the string can represent a number with
#a decimal. For example, "12.354".
