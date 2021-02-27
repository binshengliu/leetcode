from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        current_max = 0
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    dp[row][col] = (
                        min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])
                        + 1
                    )
                    current_max = max(current_max, dp[row][col])
        return current_max * current_max


s = Solution()
x = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
assert 4 == s.maximalSquare(x)
x = [["0", "1"], ["1", "0"]]
assert 1 == s.maximalSquare(x)
x = [["0"]]
assert 0 == s.maximalSquare(x)
