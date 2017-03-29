
# store previous values of function f in a cache
# function takes a function as input
# function currying style
def memoize(f):
  # create empty cache to store previously computed values of f(x)
  cache = {}
  # 
  def g(x):
    print cache
    if x not in cache:
      print x,"not in cache"
      # print "adding", f(x),"to cache for",x
      cache[x] = f(x)
    return cache[x]
  return g

def fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fib(n-2)+fib(n-1)


# pass in the function fib to memoize
# fib(n) now passes n into function g
# memoize creates and returns a new function
fib = memoize(fib)


print fib(7)