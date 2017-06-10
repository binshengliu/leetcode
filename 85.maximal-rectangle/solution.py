class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        # Add one more row for the [row-1] index in the loop
        left = [[0] * cols for i in range(rows + 1)]
        right = [[cols] * cols for i in range(rows + 1)]
        height = [[0] * cols for i in range(rows + 1)]

        max_area = 0
        for row in range(rows):
            current_left = 0
            current_right = cols
            for col in range(cols-1, -1, -1):
                if matrix[row][col] == '1':
                    right[row][col] = min(current_right, right[row-1][col])
                else:
                    current_right = col

            for col in range(cols):
                if matrix[row][col] == '1':
                    left[row][col] = max(current_left, left[row-1][col])
                    height[row][col] = height[row-1][col] + 1
                else:
                    current_left = col + 1

                width = right[row][col] - left[row][col]
                max_area = max(max_area, width * height[row][col])

        return max_area

# See:
# https://discuss.leetcode.com/topic/6650/share-my-dp-solution
