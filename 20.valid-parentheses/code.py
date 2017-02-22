class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in '}])':
                if not stack:
                    return False

                left = stack.pop()
                if left+c in ['()', '[]', '{}']:
                    continue
                return False

        return not stack
