class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []

        ans = [[1]]
        for i in range(1, numRows):
            prev_row = ans[i-1]
            current = [0] * (len(prev_row) + 1)
            current[0] = 1
            current[-1] = 1
            for j in range(1, len(prev_row)):
                current[j] = prev_row[j-1] + prev_row[j]
            ans.append(current)

        return ans
