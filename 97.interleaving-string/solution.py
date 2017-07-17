class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1 and not s2 and not s3:
            return True

        ans = False

        if s1 and s3 and s1[0] == s3[0]:
            ans = self.isInterleave(s1[1:], s2, s3[1:])

        if ans:
            return True

        if s2 and s3 and s2[0] == s3[0]:
            ans = self.isInterleave(s1, s2[1:], s3[1:])

        return ans
