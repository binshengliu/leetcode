import sys


# https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Better naming
        source = s
        target = t

        if not s or not t:
            return ''

        # Which chars to match?
        remain = {}
        for c in source:
            remain[c] = 0
        for c in target:
            remain[c] = remain.get(c, 0) + 1

        # used to formulate the answer
        head = 0
        current_len = sys.maxsize

        # active window
        begin = 0
        end = 0

        # How many chars to match?
        to_match = len(target)

        while end < len(source):
            if remain[source[end]] > 0:
                to_match -= 1
            remain[source[end]] -= 1

            while to_match == 0:
                if end - begin < current_len:
                    head = begin
                    current_len = end - begin

                if remain[source[begin]] == 0:
                    to_match += 1
                remain[source[begin]] += 1
                begin += 1

            end += 1

        ans = ''
        if current_len != sys.maxsize:
            ans = source[head:head+current_len+1]
        return ans
