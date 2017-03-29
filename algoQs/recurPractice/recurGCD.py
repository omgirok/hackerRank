# NON RECURSIVE SOLUTION
def gcd(a,b):
  start = min(a,b)
  for x in range(start,0,-1):
    if a % x == 0 and b % x == 0:
        return x


def gcd_2(a,b):
  c = min(a,b)
  if a % c == 0 and b % c == 0:
    return c
  else:
    return gcd_2(c, max(a-c,b-c))



print gcd(90,135)