"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    if head is None:
        return
    currentNode = head
    stack = []
    while currentNode.next:
        # print "now on node " + str(currentNode.data)
        stack.append(currentNode.data)
        currentNode = currentNode.next
    stack.append(currentNode.data)
    while stack:
        c = stack.pop()
        print c


  
  
  
  
