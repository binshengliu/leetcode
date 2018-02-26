# https://leetcode.com/problems/dungeon-game/discuss/52774/C++-DP-solution
#
# The key is to build up from bottom right to up left.


class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows = len(dungeon)
        cols = len(dungeon[0])
        initial = [[float('inf') for _ in range(cols + 1)]
                   for _ in range(rows + 1)]

        initial[rows - 1][cols] = 1
        initial[rows][cols - 1] = 1
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                hp = min(initial[row + 1][col],
                         initial[row][col + 1]) - dungeon[row][col]
                initial[row][col] = max(hp, 1)

        return initial[0][0]
