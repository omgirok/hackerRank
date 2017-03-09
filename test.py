from __future__ import print_function
import math

digits = ["zero","one","two","three","four","five","six","seven","eight","nine"]

def f(x):
  ret = 0

  while True:
    if x < 4:
      for i in range(x):
        ret +=1
      return ret
    else:
      x -= 4

def main():
  for n in range(9):
    print(f(n), end='')
  print()

main()

def encode(string):
  result = ''
  current = string[0]
  count = 0
  for char in string:
    if char == current:
      count+=1
    else:
      result += current
      result += str(count)
      current = char
      count = 1
  result += current
  result += str(count)
  return result

print(encode('aabccd'),encode('abcd'),encode('aaaaa'))


fibs = [0,1]
n = len(fibs)
while n < 8:
  n = len(fibs)
  fibs.append(fibs[-1] + fibs[-2])
  n+=1
print fibs[-1]