import sys


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Calculate bottom-up for each element how many steps are
        # required to reach.
        steps = [sys.maxsize for _ in range(len(nums))]
        steps[0] = 0
        for reach_index in range(1, len(nums)):
            for candidate_index in range(0, reach_index):
                can_reach = candidate_index + nums[candidate_index] >= reach_index
                if can_reach:
                    new_steps = steps[candidate_index] + 1
                    if new_steps < steps[reach_index]:
                        steps[reach_index] = new_steps

        return steps[-1]
