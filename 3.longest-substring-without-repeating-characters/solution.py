class Solution(object):
    def contain(self, c, s, start, end):
        for i in range(start, end):
            if c == s[i]:
                return True
        return False

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        # [start, end] is used as a slide window, so we need to keep
        # end across different sessions.
        end = 1
        for start in range(len(s)):
            if len(s) - start <= longest:
                break
            curr = end - start

            while end < len(s):
                if self.contain(s[end], s, start, end): # this can be
                                                        # optimized by
                                                        # using
                                                        # hashmap
                    break
                curr = curr + 1
                end = end + 1

            if curr > longest:
                longest = curr

        return longest

if __name__ == '__main__':
    s = Solution()
    string = 'abc'
    print('The length of longest substring of "{}" is {}, expect 3'.format(string, s.lengthOfLongestSubstring(string)))

    string = 'abcabcbb'
    print('The length of longest substring of "{}" is {}, expect 3'.format(string, s.lengthOfLongestSubstring(string)))

    string = 'bbbbb'
    print('The length of longest substring of "{}" is {}, expect 1'.format(string, s.lengthOfLongestSubstring(string)))

    string = 'pwwkew'
    print('The length of longest substring of "{}" is {}, expect 3'.format(string, s.lengthOfLongestSubstring(string)))

