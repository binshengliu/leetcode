class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return None

        if k == 1:
            return [[i] for i in range(1, n+1)]

        if k == n:
            return [[i for i in range(1, n+1)]]

        ans = []
        for i in range(n, k-1, -1):
            sub_ans = self.combine(i-1, k-1)
            for one in sub_ans:
                one.insert(0, i)
            ans.extend(sub_ans)
        return ans
