class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        begin = 0
        end = len(nums) - 1

        middle = 0
        while begin <= end:
            middle = int((begin + end) / 2)
            if target < nums[middle]:
                end = middle - 1
            elif target > nums[middle]:
                begin = middle + 1
            else:
                break

        left = -1
        right = -1
        # not found
        if begin > end:
            return [left, right]

        left = middle
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1
        right = middle
        while right + 1 <= len(nums) - 1 and nums[right + 1] == target:
            right += 1

        return [left, right]
