class Solution(object):
    def minimumTotalRecursive(self, triangle, row, col):
        if row == len(triangle) - 1:
            return triangle[row][col]

        return triangle[row][col] + \
            min(self.minimumTotalRecursive(triangle, row+1, col),
                self.minimumTotalRecursive(triangle, row+1, col+1))

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return None

        return self.minimumTotalRecursive(triangle, 0, 0)
