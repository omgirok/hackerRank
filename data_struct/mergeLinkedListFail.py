def MergeLists(headA, headB):
    if headA is None:
        return headB
    if headB is None:
        return headA

    # Change the next pointers to obtain a single, 
    # merged linked list also in ascending order
    
    print "checking heads: " + str(headA.data) + str(headB.data)
    # Check headA vs headB
    if headA.data < headB.data:
        currOne = headA
        currTwo = headB
    elif headB.data < headA.data:
        currOne = headB
        currTwo = headA
    
    while currOne != None and currTwo != None:
        # if currOne.next greater than currTwo, change currOne.next to currTwo.
        # change currTwo.next to currOne.next
        # currTwo goes to next
        # currOne goes to next
        curr = currOne
        nextOne = currOne.next
        nextTwo = currTwo.next

        print "list 1 now on: " + str(currOne.data)
        print "list 2 now on: " + str(currTwo.data)
        if nextOne > nextTwo:
            curr.next = currTwo
            curr = curr.next
            currOne = currOne.next
            currTwo = currTwo.next
        else:
            curr.next = currOne
            curr = curr.next