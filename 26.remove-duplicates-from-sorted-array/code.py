class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        i = 0
        while i < len(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                del nums[i]
                continue
            i += 1
            n += 1
        return n
