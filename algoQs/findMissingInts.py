"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        set1 = set(range(1,len(nums)+1))
        set2 = set(nums)
        result = list(set1 - set2)
        return result

    def findDisappearedNumbers_2(self, nums):
        for i in nums:
        index = abs(i)-1
        nums[index] = -abs(nums[index])
        
        return [x+1 for x in range(len(nums)) if nums[x] > 0]