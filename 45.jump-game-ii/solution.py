import sys


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dist = [sys.maxsize for index in range(0, len(nums))]
        dist[0] = 0
        unvisited = set([index for index in range(0, len(nums))])

        while unvisited:
            # Find the shortest index
            shortest_index = None
            shortest_step = sys.maxsize
            for index in unvisited:
                if dist[index] < shortest_step:
                    shortest_index = index
                    shortest_step = dist[index]

            if shortest_index == len(nums) - 1:
                return shortest_step

            unvisited.remove(shortest_index)

            # do relax
            max_reach = min(len(nums), shortest_index+nums[shortest_index]+1)
            for index in range(shortest_index+1, max_reach):
                if shortest_step + 1 < dist[index]:
                    dist[index] = shortest_step + 1

        raise ValueError("This should not be reached.")
