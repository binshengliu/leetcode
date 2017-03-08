'''Use a stack to find mismatches. The difference of adjacent
mismatches must be a valid sequence'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for (i, char) in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack and s[stack[-1]] == '(':
                    del stack[-1]
                else:
                    stack.append(i)
            else:               # defensive
                raise ValueError('The input contains illegal characters.')

        if not stack:
            return len(s)

        # test the case of '(()'
        stack.append(len(s))

        longest = 0
        prev = -1
        for i in stack:
            if i - prev - 1 > longest:
                longest = i - prev - 1
            prev = i

        return longest
