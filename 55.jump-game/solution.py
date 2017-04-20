class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) <= 1:
            return True

        farthest = 0
        end = 0
        jumps = 0
        for i in range(len(nums)):
            if i + nums[i] > farthest:
                farthest = i + nums[i]
                if farthest >= len(nums) - 1:
                    return True

            if i == end:
                jumps += 1
                end = farthest

                # if after jumping, end is still here and current
                # available step is zero, there's no chance we can go
                # further
                if i == end and nums[i] == 0:
                    return False

        return False
