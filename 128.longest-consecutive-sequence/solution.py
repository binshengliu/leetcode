class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        nums = set(nums)
        for num in nums:
            if num - 1 in nums:
                continue

            t = num + 1
            while t in nums:
                t += 1

            longest = max(longest, t - num)

        return longest
