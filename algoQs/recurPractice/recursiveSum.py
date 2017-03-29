def summ(x):
  if x == 1:
    return 1
  else:
    return x + summ(x-1)

def sumSeries(n):
  if n <= 0:
    return 0
  else:
    return n + sumSeries(n-2)

def main():
  print "returning sum of all integers from 1,2,3...10"
  print summ(10)


  print "returning sum of all integers from 24,22,20,18,16...0"
  print sumSeries(24)

main()