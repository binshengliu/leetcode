# Let S(k) denote whether the length k prefix can be segmented. The
# problem can be split into two subproblems recursively. We choose a
# position k such that S[:k] and S[k:] can both be broken. There may
# be many ks for a string. In this problem, we only need to find one.
# To simplify the problem, we find k where S[k:] is the last shortest
# valid word segment.
#
# Recursive definition of the problem:
#
# S(0) = True
# S(n) = S(k) and string[k:] in dict for k in range(0, n)

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        table = [False for i in range(n + 1)]
        table[0] = True

        wordDict = set(wordDict)

        for i in range(1, n + 1):
            for j in range(0, i):
                if table[j] and s[j:i] in wordDict:
                    table[i] = True
                    break

        return table[n]
