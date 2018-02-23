# https://leetcode.com/problems/maximum-product-subarray/discuss/48261/Share-my-DP-code-that-got-AC
#
# The key to this DP solution is storing the minimum value at i as
# well as the maximum value.
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Maximum product containing nums[i]
        maximum = [None for _ in range(n)]

        # Minimum product containing nums[i]
        minimum = [None for _ in range(n)]

        maximum[0] = nums[0]
        minimum[0] = nums[0]
        global_max = nums[0]
        for i in range(1, n):
            maximum[i] = max(nums[i], nums[i] * maximum[i-1], nums[i] * minimum[i-1])
            minimum[i] = min(nums[i], nums[i] * maximum[i-1], nums[i] * minimum[i-1])

            global_max = max(global_max, maximum[i])

        return global_max
