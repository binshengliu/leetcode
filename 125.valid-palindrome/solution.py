class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:
            while left <= len(s)-1 and not s[left].isalnum():
                left += 1

            while right >= 0 and not s[right].isalnum():
                right -= 1

            if left <= len(s) - 1 and right >= 0 and s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
