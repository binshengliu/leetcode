from operator import attrgetter


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
        intervals.sort(key=attrgetter('start'))
        ans = []

        index = 0
        while index < len(intervals):
            current = intervals[index]
            merged = 0
            for interval in intervals[index+1:]:
                if interval.start <= current.end:
                    merged += 1
                    current.end = max(current.end, interval.end)
                else:
                    break

            ans.append(current)
            index += merged + 1

        return ans
