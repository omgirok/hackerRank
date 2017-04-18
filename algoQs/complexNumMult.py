"""
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
"""

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1,a2 = a[:-1].split('+')
        print a1,a2
        b1,b2 = b[:-1].split('+')
        print b1,b2
        
        # FOIL = (a1*b1) + (a1*b2)i + (a2*b1)i + (a2*b2)(-1)        
        F = int(a1)*int(b1)
        O = int(a1)*int(b2)
        I = int(a2)*int(b1)
        L = int(a2)*int(b2)*(-1)
        
        result = "%d+%di" % (F+L, O+I)
        return result