class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1

        while begin <= end:
            middle = int((begin + end) / 2)

            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                end = middle - 1
            else: # nums[middle] < target
                begin = middle + 1

        return begin
