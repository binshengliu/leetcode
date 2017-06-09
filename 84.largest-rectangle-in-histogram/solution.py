class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = []
        heights.append(0)
        for (index, height) in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                current_index = stack[-1]
                del stack[-1]
                width = (index - stack[-1] - 1) if stack else index
                area = heights[current_index] * width
                if area > max_area:
                    max_area = area

            stack.append(index)

        return max_area

# See:
# https://discuss.leetcode.com/topic/3913/my-concise-c-solution-ac-90-ms
# https://discuss.leetcode.com/topic/7599/o-n-stack-based-java-solution
# http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
