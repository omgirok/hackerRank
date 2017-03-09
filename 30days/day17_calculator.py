import math

# Calculator class that does exponential math.
# parameters must be positive otherwise it will throw an exception
# Exception handling example

class Calculator:
    def power(self,n,p):
        # Throws an exception if n or p is negative
        if (n < 0) or (p < 0):
            raise ValueError("n and p should be non-negative.")
        else:
            return math.pow(n,p)

calc = Calculator()
try:
    print int(calc.power(2,5))
    print int(calc.power(-1,-4))
except Exception, e:
    print e
