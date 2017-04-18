"""
  Write a function that given n, where n is the length of a string,
  Generate all binary numbers of length n

"""

import copy

def genBinary(string,n):
  if n == 0:
    print string
  elif n > 0:
    genBinary(string+'1', n-1)
    genBinary(string+'0', n-1)

def genBinary_2(n):
  if n == 0:
    return []
  if n == 1:
    # print "base"
    return ['0','1']
  if n > 1:
    # print n
    n_0 = genBinary_2(n-1)
    n_1 = copy.deepcopy(n_0)
    # print n_0,n_1

    for i in n_0:

      y = n_0.pop()
      # print y
      n_0.insert(0,'0'+y)
    for i in n_1:
      y = n_1.pop()
      n_1.insert(0,'1'+y)

    return n_0+n_1

if __name__ == "__main__":
  # print "hi"
  # print genBinary_2(3)
  # print genBinary_2(4)
  print genBinary_2(3)


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

