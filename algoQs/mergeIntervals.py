# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        for i in sorted(intervals,key=lambda interval: interval.start):
            if result and i.start <= result[-1].end:
                result[-1].end = max(result[-1].end, i.end)
            else:
                result.append(i)
        return result

    def merge_2(self, intervals, index):
        if index > len(intervals) or len(intervals) <= 1:
            return intervals
        toCheck = intervals.pop(index)
        toCheck2 = intervals.pop(index)
        if toCheck2.start <= toCheck.end:
            newInt = Interval(toCheck.start, toCheck2.end)
            intervals.insert(index,newInt)
            return self.merge_2(intervals, index)
        else:
            return self.merge_2(intervals, index+1)


            
