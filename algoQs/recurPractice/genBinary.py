"""
  Write a function that given n, where n is the length of a string,
  Generate all binary numbers of length n

"""


def genBinary(string,n):
  if n == 0:
    print string
  elif n > 0:
    genBinary(string+'1', n-1)
    genBinary(string+'0', n-1)

def genBinary_2(n):
  

genBinary('', 1)


"""
f(1) = '1', '0'
f(2) = '11', '10', '01', '00'
f(3) = '111', '110', '101', '100', '011', '010', '001', '000'
"""

# def genBinaryArr(n):
#   output = []
#   if n == 0:
#     return output
#   elif n > 0:

