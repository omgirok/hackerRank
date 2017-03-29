def fibonacci(n):
  print "prints fibonacci sequence up to",n+1,"numbers"
  i = 0
  j = 1
  
  for x in range(n):
    s = i+j
    if x == 0:
      print "%d" %(i),
    if x == 1:
      print "%d" %(j),
    else:
      print "%d" %(s),
      i = j
      j = s

fibonacci(9)

