# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # import pudb.b

        index = 0
        for interval in intervals:
            if newInterval.start <= interval.start:
                break
            index += 1
        intervals.insert(index, newInterval)

        ans = []
        index = 0
        while index < len(intervals):
            current = intervals[index]
            merged = 0
            for interval in intervals[index+1:]:
                if interval.start <= current.end:
                    current.end = max(current.end, interval.end)
                    merged += 1
                else:
                    break

            ans.append(current)
            index += merged + 1

        return ans
