import sys


class Solution(object):
    def _jump(self, nums, current_index):
        """find steps needed from current_index to the last element
        :rtype: int
        """
        if current_index == len(nums) - 1:
            return 0

        min_steps = sys.maxsize
        for candidate in range(current_index+1, current_index+nums[current_index]+1):
            steps = self._jump(nums, candidate)
            if steps < min_steps:
                min_steps = steps

        return min_steps + 1

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        steps = self._jump(nums, 0)
        return steps
