# find from rear to head, the first element that is smaller than any one of the digit after it

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for (i, num) in reversed(list(enumerate(nums))):

            for begin in range(i + 1, len(nums)):
                if num < nums[begin]:
                    nums[i], nums[begin] = nums[begin], nums[i]
                    return

            for begin in range(i + 1, len(nums)):
                nums[begin - 1] = nums[begin]

            nums[len(nums) - 1] = num
