class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print nums
        for i, val1 in enumerate(nums):
            for j, val2 in enumerate(nums):
                if i == j:
                    continue
                if val1 + val2 == target:
                    return [i, j]
        return [0, 0]

s = Solution()
print s.twoSum([3,2,4], 6)
