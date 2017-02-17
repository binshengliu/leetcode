class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {1:'*', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz', 0:' '}

        ans = []
        for c in digits:
            if ans:
                s = []
                for e in ans:
                    for j in mapping[int(c)]:
                        s.append(e + j)
                ans = s
            else:
                for i in mapping[int(c)]:
                    ans.append(i)

        return ans
