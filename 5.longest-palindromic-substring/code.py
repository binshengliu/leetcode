class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # print("Arguments: {}".format(s))

        ret = ''
        for i, c in enumerate(s):
            print("\ni: {}, c: {}".format(i, c))

            curr = 0
            left = i - 1
            right = i + 1
            begin = i
            end = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr = curr + 1
                begin = left
                end = right
                left = left - 1
                right = right + 1

            if end - begin + 1 > len(ret):
                ret = s[begin:end + 1]

            # print("Situation 1: curr: {}, left: {}, right: {}".format(curr, left, right))
            # print("begin: {}, end: {}, ret: {}".format(begin, end, ret))

            curr = 0
            left = i
            right = i + 1
            begin = i
            end = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr = curr + 1
                begin = left
                end = right
                left = left - 1
                right = right + 1

            if end - begin + 1 > len(ret):
                ret = s[begin:end + 1]

            # print("\nSituation 2: curr: {}, left: {}, right: {}".format(curr, left, right))
            # print("begin: {}, end: {}, ret: {}".format(begin, end, ret))
        return ret

if __name__ == '__main__':
    s = Solution()
    # string = 'babad'
    # ret = s.longestPalindrome(string)
    # print("Result: {}".format(ret))

    # string = 'cbbd'
    # ret = s.longestPalindrome(string)
    # print("Result: {}".format(ret))

    string = 'ccc'
    ret = s.longestPalindrome(string)
    print("Result: {}".format(ret))
