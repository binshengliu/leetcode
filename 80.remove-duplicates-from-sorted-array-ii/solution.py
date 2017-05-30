class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        n = 2
        i = 2
        while i < len(nums):
            if nums[i] != nums[n - 1] or nums[i] != nums[n - 2]:
                nums[n] = nums[i]
                n += 1
            i += 1
        return n
