class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        dp = [[triangle[0][0]]]
        for row in range(1, len(triangle)):
            new_row = []
            for col in range(len(triangle[row])):
                cur_value = triangle[row][col]
                if col == 0:
                    prev_min = dp[row-1][0]
                elif col == len(triangle[row]) - 1:
                    prev_min = dp[row-1][col-1]
                else:
                    prev_min = min(dp[row-1][col-1], dp[row-1][col])
                new_row.append(cur_value + prev_min)
            dp.append(new_row)

        return min(dp[-1])
