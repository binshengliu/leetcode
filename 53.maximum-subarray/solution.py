

# https://discuss.leetcode.com/topic/6413/dp-solution-some-thoughts
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # As somebody pointed out in the link, there's no need to
        # record dp, but I'll leave it for clarity.
        dp = [None for _ in nums]
        dp[0] = nums[0]
        current_max = dp[0]
        for (i, num) in enumerate(nums[1:], 1):
            dp[i] = max(dp[i-1] + num, num)
            current_max = max(current_max, dp[i])

        return current_max
