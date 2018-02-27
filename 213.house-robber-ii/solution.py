class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        return max(self.rob_dp(nums[:-1]), self.rob_dp(nums[1:]))

    def rob_dp(self, nums):
        n = len(nums)
        dp = [0 for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        return dp[0]
