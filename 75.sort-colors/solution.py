class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        i = 0
        two_pos = len(nums) - 1
        while i <= two_pos:
            if nums[i] == 2:
                nums[i], nums[two_pos] = nums[two_pos], nums[i]
                two_pos -= 1
            else:
                i += 1

        i = two_pos
        zero_pos = 0
        while i >= zero_pos:
            if nums[i] == 0:
                nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
                zero_pos += 1
            else:
                i -= 1
