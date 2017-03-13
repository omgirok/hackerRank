"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
    if headA is None and headB is None:
        return None
    if headA is None:
        return headB
    if headB is None:
        return headA

    # Change the next pointers to obtain a single, 
    # merged linked list also in ascending order
    print "checking heads: " + str(headA.data) + " & " + str(headB.data)
    
    if headA.data < headB.data:
        currOne = headA
        currTwo = headB
    elif headB.data < headA.data:
        currOne = headB
        currTwo = headA

    ret = prev = currOne
    currOne = currOne.next
    while currOne and currTwo:

        # print "list 1 now on: " + str(currOne.data)
        # print "list 2 now on: " + str(currTwo.data)
        if currOne.data < currTwo.data:
            prev = currOne
            currOne = currOne.next
        else:
            prev.next = currTwo
            prev_currTwo = currTwo
            currTwo = currTwo.next
            prev_currTwo.next = currOne

    if currTwo:
        prev.next = currTwo
        
    return ret

"""

  1 -> 3 -> 4 -> 6 -> 7 -> NULL


  2 -> 5 -> 6 -> NULL

  1 -> 2 -> 3
"""







    

  
  
  
  
  
  
  
  
  
  
  
