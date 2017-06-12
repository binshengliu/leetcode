
# Another solution is to swap the current value with the last one

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        j = 0
        for (_, elem) in enumerate(nums):
            if elem != val:
                nums[j] = elem
                j += 1
        return j
