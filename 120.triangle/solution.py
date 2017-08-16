class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        dp = [triangle[0][0]]
        for row in range(1, len(triangle)):
            new_row = [0] * len(triangle[row])
            for col in range(len(triangle[row])):
                cur_value = triangle[row][col]
                if col == 0:
                    prev_min = dp[0]
                elif col == len(triangle[row]) - 1:
                    prev_min = dp[col-1]
                else:
                    prev_min = min(dp[col-1], dp[col])
                new_row[col] = cur_value + prev_min
            dp = new_row

        return min(dp)
