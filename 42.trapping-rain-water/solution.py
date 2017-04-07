from operator import itemgetter


# 1. Find the two largest elevation
# 2. Calculate the area between them
# 3. Calculate the left part and right part recursively
# 4. Add the three parts
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0

        sorted_with_index = sorted(enumerate(height),
                                   key=itemgetter(1), reverse=True)

        largest = sorted_with_index[0]
        second_largest = sorted_with_index[1]

        small_index = min(largest[0], second_largest[0])
        large_index = max(largest[0], second_largest[0])
        largest_area = min(largest[1], second_largest[1]) \
            * (large_index - small_index - 1)

        current_area = largest_area
        for inside_index in range(small_index + 1, large_index):
            current_area -= height[inside_index]

        left_area = self.trap(height[:small_index+1])
        right_area = self.trap(height[large_index:])

        total_area = left_area + current_area + right_area

        return total_area
