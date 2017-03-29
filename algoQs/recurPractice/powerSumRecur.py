"""
Find the number of ways that a given integer, X, 
can be expressed as the sum of the N power of unique, natural numbers.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
x = input("enter number to find sum: ")
n = input("enter power: ")


def powerSum(x,n,m):
    count = 0
    # need to see if integers**n sum up to x
    # try to take all numbers y to the power of n and see if the sum equals x
    highest = int(x**(1/float(n)))
    print "only need to check up to",highest
    if m < highest:
        highest = m
    for y in range(highest,0,-1):
        # print y
        power = y**n
        print power,x
        if x == power:
            print "found a sum"
            count+=1
            # numbers.append(y)
        else:
            # 
            newTotal = x - power
            count += powerSum(newTotal,n,y-1)

    return count

print powerSum(x,n,x)



            
        