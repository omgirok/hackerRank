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
		ss = str(negate(reverse(pathOfPaper(n-1))))


		return s + "R" + ss

print pathOfPaper(1)
print pathOfPaper(2)
print pathOfPaper(3)
print pathOfPaper(5)

