'''https://leetcode.com/articles/longest-valid-parentheses/#approach-2-using-dynamic-programming-accepted'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for char in s]

        cur_max = 0
        for (i, char) in enumerate(s):
            if char == ')':
                if i - 1 >= 0 and s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i - 2 >= 0 else 2
                elif i - 1 >= 0 and s[i - 1] == ')':
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2 if \
                        i - dp[i - 1] - 2 >= 0 else dp[i - 1] + 2
                if dp[i] > cur_max:
                    cur_max = dp[i]

        return cur_max
