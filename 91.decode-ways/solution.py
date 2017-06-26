class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        if s[0] == '0':
            return 0

        if len(s) == 1:
            return 1

        if len(s) == 2:
            if s[0] == '1':
                if s[1] == '0':
                    return 1
                else:
                    return 2
            elif s[0] == '2':
                if s[1] == '0':
                    return 1
                elif s[1] in '123456':
                    return 2
                else:
                    return 1
            elif s[1] == '0':
                return 0
            else:
                return 1

        ans = 0
        if s[0] == '1':
            if s[1] == '0':
                ans += self.numDecodings(s[2:])
            else:
                ans += self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        elif s[0] == '2':
            if s[1] == '0':
                ans += self.numDecodings(s[2:])
            elif s[1] in '123456':
                ans += self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            else:
                ans += self.numDecodings(s[1:])
        else:
            ans += self.numDecodings(s[1:])

        return ans
