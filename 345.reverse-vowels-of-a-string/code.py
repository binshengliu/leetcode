class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        reversedVowels = []
        newWord = []
        for c in s:
            if c in vowels:
                reversedVowels.insert(0, c)

        i = 0
        for c in s:
            if c in vowels:
                newWord.append(reversedVowels[i])
                i = i + 1
            else:
                newWord.append(c)

        return ''.join(newWord)

s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels('leetcode'))
