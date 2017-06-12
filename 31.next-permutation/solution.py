# find from rear to head, the first element that is smaller than any one of the digit after it

class Solution(object):
    def reverse(self, nums, begin, end):
        l = begin
        r = end - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        swap = len(nums) - 2
        while swap >= 0:
            if nums[swap] < nums[swap + 1]:
                break
            swap -= 1

        if swap >= 0:
            to_swap = swap
            while to_swap <= len(nums) - 2:
                if nums[to_swap + 1] <= nums[swap] < nums[to_swap]:
                    break
                to_swap += 1

            nums[swap], nums[to_swap] = nums[to_swap], nums[swap]
            self.reverse(nums, swap + 1, len(nums))
        else:
            self.reverse(nums, 0, len(nums))
