

# Refer to this link:
# https://discuss.leetcode.com/topic/28470/concise-o-n-one-loop-java-solution-based-on-greedy/2
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        farthest = 0
        end = 0
        jumps = 0
        for (i, num) in enumerate(nums[:-1]):
            if i + num > farthest:
                farthest = i + num
            if i == end:
                jumps += 1
                end = farthest

        return jumps
