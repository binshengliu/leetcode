class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []

        if rowIndex == 0:
            return [1]

        ans = []
        prev_row = [1]
        for i in range(1, rowIndex+1):
            ans = [0] * (i+1)
            ans[0] = 1
            ans[-1] = 1
            for j in range(1, i):
                ans[j] = prev_row[j-1] + prev_row[j]
            prev_row = ans

        return ans
