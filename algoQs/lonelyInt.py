#!/usr/bin/py
import copy

def lonelyinteger(a):
    set1 = set()
    b = copy.deepcopy(a)
    list.sort(b)
    for y in range(len(a)):
        el = a.pop()
        set1.add(el)
    # fill set1 with all unique values of array
    for x in set1:
        # iteratively remove single element from b
        # and from set1
        # after removing element from b and from set1, it should still exist in b
        el = x
        b.remove(el)
        if el not in b:
            return el
        
    # result = [item for item in b if item not in set1]
    # return result[0] 
        
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
