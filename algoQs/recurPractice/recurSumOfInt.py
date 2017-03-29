# recursively sum the digits of the integer
# 
# return x        when x < 10
# return x%10 + x/10 when x > 10
def sumOfInt(n):
  if n < 10:
    return n
  else:
    return n%10 + sumOfInt(n/10)

print sumOfInt(413239)
