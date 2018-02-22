class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        wordDict = set(wordDict)
        table = [False for _ in range(n + 1)]
        table[0] = True
        for i in range(1, n + 1):
            for split in range(i):
                if table[split] and s[split:i] in wordDict:
                    table[i] = True
                    break

        return construct(s, wordDict, table, n)


def construct(s, wordDict, table, length):
    result = set()
    if s[:length] in wordDict:
        result.add(s[:length])
    for i in range(length - 1, 0, -1):
        word = s[i:length]
        if table[i] and word in wordDict:
            sub_result = construct(s, wordDict, table, i)
            for one in sub_result:
                result.add(' '.join([one, word]))
    return [i for i in result]
