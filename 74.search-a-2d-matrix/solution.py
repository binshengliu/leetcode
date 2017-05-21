class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        row_beg = 0
        row_end = rows - 1

        col_beg = 0
        col_end = cols - 1

        while row_beg <= row_end:
            row_mid = int((row_beg+row_end) / 2)
            if target < matrix[row_mid][0]:
                row_end = row_mid - 1
                continue
            elif matrix[row_mid][cols-1] < target:
                row_beg = row_mid + 1
                continue

            # Now, matrix[row_mid][0] <= target <= matrix[row_mid][cols-1]
            while col_beg <= col_end:
                col_mid = int((col_beg + col_end) / 2)
                if target < matrix[row_mid][col_mid]:
                    col_end = col_mid - 1
                    continue
                elif matrix[row_mid][col_mid] < target:
                    col_beg = col_mid + 1
                    continue
                return True
            return False
        return False
