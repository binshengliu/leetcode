class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        table = [[False for col in range(n)] for row in range(n)]

        wordDict = set(wordDict)

        for i in range(0, n):
            for j in range(i, n):
                row = j - i
                col = j
                exist = False

                if s[row:col+1] in wordDict:
                    table[row][col] = True
                    continue

                for split in range(row, col):
                    table[row][col] = table[row][split] and table[split+1][col]
                    if table[row][col]:
                        break

        return table[0][n-1]


def test_1():
    wordDict = ['leet', 'code']
    word = 'leetcode'
    s = Solution()
    result = s.wordBreak(word, wordDict)
    assert(result)
