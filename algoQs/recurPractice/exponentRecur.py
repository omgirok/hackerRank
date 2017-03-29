# @trace
def exponents(x, n):
  """
  Computes the result of x raised to the power of n.

      >>> exponents(2, 3)
      8
      >>> exponents(3, 2)
      9
  """
  # print "now on call/stack frame: x: " + str(x) + ", n: " + str(n)
  if n == 0:
    # print "n = 0! returning 1..."
    return 1
  else:
    # print "executing x(" + str(x) + ") * exp(x," + str(n-1)+")"
    return x * exponents(x, n-1)

  """
  Execution pattern visualized:
    exp(2, 4)
    +-- 2 * exp(2, 3)
    |       +-- 2 * exp(2, 2)
    |       |       +-- 2 * exp(2, 1)
    |       |       |       +-- 2 * exp(2, 0)
    |       |       |       |       +-- 1
    |       |       |       +-- 2 * 1
    |       |       |       +-- 2
    |       |       +-- 2 * 2
    |       |       +-- 4
    |       +-- 2 * 4
    |       +-- 8
    +-- 2 * 8
    +-- 16
  """

print exponents(2,4)