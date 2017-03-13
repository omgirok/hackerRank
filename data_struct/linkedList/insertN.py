"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    newNode = Node()
    newNode.data = data
    # print "position is:", position
    currentNode = head
    prev = currentNode
    i = 0
    if position == 0:
        newNode.next = currentNode
        head = newNode
    else:
        while i in range(position):
            # print "now on index:", i
            prev = currentNode
            currentNode = currentNode.next
            i+=1
        prev.next = newNode
        newNode.next = currentNode
    
    return head
    
  
  
  
  
  
  
  
  
  
  
