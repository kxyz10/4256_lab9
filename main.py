import math;
class Fraction:
  #the constructor for the Fraction class
  #n is the numerator
  #d is the denominator
  #The constructor should create a Fraction object that is reduced
  def __init__(self, num, den = None):
    if den == None:
      slashLoc = num.find('/')
      numerator = float(num[0:slashLoc])
      denominator = float(num[slashLoc+1:len(num)])
      num = numerator
      den = denominator
    if type(num) != float or type(den) != float:
      gcd = math.gcd(num,den)
    else:
      gcd = 1
    #if gdc == 1 these lines do nothing
    num = num / gcd
    den = den / gcd
    if den < 0 and num >= 0:
      den = -1 * den
      num = -1 * num
    if den < 0 and num < 0:
      den = -1 * den
      num = -1 * num
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
    temp = self.num
    self.num = self.den
    self.den = temp

  #If f is a Fractions, then -f returns a Fraction that is the
  # negation of f. 
  def __neg__(self):
    self.num = -1 * self.num

  #If f and g are Fractions, then f + g returns a Fraction that is the
  # sum of f and g
  def __add__(self, other):
    if self.den == other.den:
      return Fraction(int(self.num + other.num), int(self.den))
    else:
      prod = self.den * other.den
      selfNum = self.num * other.den
      otherNum = other.num * self.den
      return Fraction(int(selfNum + otherNum), int(prod))



  #If f and g are Fractions, then f - g returns a Fraction that is the
  # difference of f and g
  #You should implement this method without calling the constructor directly.
  def __sub__(self, other):
    if self.den != other.den:
      self.num = self.num * other.den
      other.num = other.num * self.den
      self.den = self.den * other.den
      other.den = other.den * self.den
    if self.num >= other.num:
      self.num = self.num - other.num
    else:
      self.num = 0 - (other.num - self.num)
    return self
      

  #If f and g are Fractions, then f / g returns a Fraction that is the
  # quotient of f and g
  #You should implement this method without calling the constructor directly.
  def __truediv__(self, other):
    self.num = self.num * other.den
    self.den = self.den * other.num
    return self

  #Returns true if self < other. False otherwise
  def __lt__(self, other):
    return self.num/self.den < other.num/other.den

  #Returns the absolute value of self. If f is a Fraction, this is called as abs(f).
  def __abs__(self):
    if self.num < 0:
      self.num = self.num * -1
    return self

  ##Returns a string representation of self as a mixed number. For example, 12/5 as a mixed number is "2 2/5".
  def mixed_number(self):
    if self.num > self.den:
      number = int(self.num / self.den)
      remainder = self.num % self.den
      return "{} {}/{}".format(number, remainder, self.den)
    else:
      return "{}/{}".format(self.num,self.den)

#After you finish and test all of the methods above, you should modify the __init__ methods so that it can be passed a string
#representation of a fraction, such as "14/102". To do this, modify the definition of __init__ as shown below,

#__init__(self, n, d = None):

#In your code, check to see if d is None. If it is, then n holds the string representation. If d is not None,
#then n and d are integers representing the numerator and denominator respectively.

#Finally, modify your code so that the string can represent a number with
#a decimal. For example, "12.354".
