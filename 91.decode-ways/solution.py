cache = {}


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s in cache:
            return cache[s]

        if not s:
            cache[s] = 0
            return 0

        if s[0] == '0':
            cache[s] = 0
            return 0

        if len(s) == 1:
            cache[s] = 1
            return 1

        if len(s) == 2:
            if s[0] == '1':
                if s[1] == '0':
                    cache[s] = 1
                    return 1
                else:
                    cache[s] = 2
                    return 2
            elif s[0] == '2':
                if s[1] == '0':
                    cache[s] = 1
                    return 1
                elif s[1] in '123456':
                    cache[s] = 2
                    return 2
                else:
                    cache[s] = 1
                    return 1
            elif s[1] == '0':
                cache[s] = 0
                return 0
            else:
                cache[s] = 1
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

        cache[s] = ans
        return ans
