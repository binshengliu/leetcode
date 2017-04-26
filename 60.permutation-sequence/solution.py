class Solution(object):
    def getPermutationRecursively(self, l, k):
        if not l:
            return [[]]

        ans = []
        for (i, num) in enumerate(l):
            first = num
            rest = l[:i] + l[i+1:]
            sub_ans = self.getPermutationRecursively(rest, k)
            for one_list in sub_ans:
                one_list.insert(0, first)
            ans.extend(sub_ans)

        return ans

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        l = [i for i in range(1, n+1)]

        sub_ans = self.getPermutationRecursively(l, k)

        return ''.join([str(i) for i in sub_ans[k-1]])
