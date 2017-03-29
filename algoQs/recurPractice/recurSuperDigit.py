"""
  Find the super digit of n repeated k times
"""

n = input("enter number to find super digit of: ")
k = input("enter how many times to repeat this number: ")

def sumDigits(n):
  if int(n) < 10:
    return int(n)
  else:
    total = 0
    for x in n:
      total+=int(x)
    # print "summing digits of",n,"equals",total
    return sumDigits(str(total))

def superDigit(n,k):
  if int(n) < 10:
    return n
  n = str(n)
  # sum up digits before k and then multiply by k
  total = sumDigits(n)  
  # print "total of digits before k is:",total
  p = total*k
  p = str(p)

  return sumDigits(p)


print superDigit(n,k)