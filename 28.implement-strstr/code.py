class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == '' and needle == '':
            return 0

        length = len(needle)
        for (i, _) in enumerate(haystack):
            if needle == haystack[i : i + length]:
                return i
        return -1
