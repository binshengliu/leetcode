class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        n = len(strs)
        first = strs[0]
        for i, c in enumerate(first):
            for s in strs[1:]:
                if i >= len(s):
                    return s[:i]

                if s[i] != c:
                    return s[:i]
        return first
