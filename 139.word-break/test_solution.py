from solution import Solution

def test_1():
    wordDict = ['leet', 'code']
    word = 'leetcode'
    s = Solution()
    result = s.wordBreak(word, wordDict)
    assert(result)


def test_2():
    wordDict = ['a', 'code']
    word = 'a'
    s = Solution()
    result = s.wordBreak(word, wordDict)
    assert(result)
