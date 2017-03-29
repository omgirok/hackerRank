"""
  Thinking recursively, 
  the max of a list is either the first element 
  OR
  the maximum in the rest of the list
  if list only has size 1 then that is the biggest number
"""

def maxOfList(arr):
  # base case is when size of the array is 1
  if len(arr) == 1:
    print "only one element in array. returning", arr[0]
    return arr[0]
  else:
    # max of list is either the first element
    A = arr[0]
    # or the maximum of the rest of that list
    B = arr[1:len(arr)]
    print "now comparing " + str(A) + " with the max of " + str(B)
    
    biggest = max(A,maxOfList(B))
    # print "largest is: " + str(biggest)
    return biggest


arr = [6,2,30,4,5]
print "max of the array " + str(arr) + " is: " + str(maxOfList(arr))