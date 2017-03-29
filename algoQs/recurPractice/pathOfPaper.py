"""
  Write an algorithm that will return the path of a piece of paper
  that is folded in half to the right n times.
  For a strip of paper that is folded in half once (n = 1) and to the right,
  the path is a single right turn so the algorithm should return "R"
  For n = 2, the path is RRL
  For n = 3, the path is RRLRRLL
  For n = 4, the path is RRLRRLLRRRLLRLL and so on...
"""

def negate(s):
	x=0
	ss = list(s)
	while x < len(ss):
		if ss[x] == 'L':
			ss[x] = 'R'
		elif ss[x] == 'R':
			ss[x] = 'L'
		x = x+1
	sss = ''.join(ss)
	return sss

def reverse(s):
	s = ''.join(reversed(s))
	return s

def pathOfPaper(n):
	if n == 0:
		return ""
	elif n >= 1:
		s = pathOfPaper(n-1)
		ss = str(negate(reverse(s)))


		return s + "R" + ss

print pathOfPaper(1)
print pathOfPaper(2)
print pathOfPaper(3)
print pathOfPaper(5)

