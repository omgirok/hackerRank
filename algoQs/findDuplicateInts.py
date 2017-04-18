"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        results = {}
        ans = []
        for i in xrange(len(nums)):
            results[nums[i]] = 0
        for i in xrange(len(nums)):
            results[nums[i]]+=1
        
        for x in results:
            if results[x] == 2:
                ans.append(x)
        return ans

    def findDuplicates_2(self, nums):
        ans = []
        for i in nums:
            if nums[i] > 0:
                nums[i] = -nums[i]
            else:
                ans.append(abs(nums[i]))
        return ans

