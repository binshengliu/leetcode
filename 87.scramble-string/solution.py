class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        length = len(s1)
        for i in range(1, length):
            sub_ans = self.isScramble(s1[:i], s2[:i]) and \
                self.isScramble(s1[i:], s2[i:])
            if sub_ans:
                return True

            sub_ans = self.isScramble(s1[:i], s2[length-i:]) and \
                self.isScramble(s1[i:], s2[:length-i])
            if sub_ans:
                return True

        return False

# See:
# https://discuss.leetcode.com/topic/14337/share-my-4ms-c-recursive-solution

# If s1 is a scrambled string of s2, then there must be a point i,
# where (s1[:i] s2[:i]) and (s1[i:] s2[i:]) are scrambled strings of
# each other, or (s1[:i], s2[len-i:]) and (s1[i:], s2[:len-i]) are
# scrambled strings of each other.
