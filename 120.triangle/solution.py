class Solution(object):
    def minimumTotalRecursive(self, triangle, row, col):
        if (row, col) in self.hashmap:
            return self.hashmap[(row, col)]

        if row == len(triangle) - 1:
            return triangle[row][col]

        value = triangle[row][col] + \
            min(self.minimumTotalRecursive(triangle, row+1, col),
                self.minimumTotalRecursive(triangle, row+1, col+1))

        self.hashmap[(row, col)] = value
        return value

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return None

        self.hashmap = {}
        return self.minimumTotalRecursive(triangle, 0, 0)
