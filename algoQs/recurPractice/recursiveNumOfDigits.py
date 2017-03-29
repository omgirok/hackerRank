def numDigits(n):
  if n < 10:
    return 1
  else:
    return 1 + numDigits(n/10)


print "checking num of digits in 10: " + str(numDigits(10))
print "checking num of digits in 123: " + str(numDigits(123))