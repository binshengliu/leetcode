class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        n = 1
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums[n] = nums[i]
                n += 1
            i += 1
        return n
