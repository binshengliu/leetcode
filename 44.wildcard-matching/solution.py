

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        match = [[False for pattern_index in range(len(p)+1)]
                 for str_index in range(len(s)+1)]
        match[0][0] = True

        for (pattern_index, pattern_char) in enumerate(p, 1):
            if pattern_char == '*':
                match[0][pattern_index] = match[0][pattern_index-1]

        for (str_index, str_char) in enumerate(s, 1):
            for (pattern_index, pattern_char) in enumerate(p, 1):
                if (str_char == pattern_char) or (pattern_char == '?'):
                    match[str_index][pattern_index] = \
                        match[str_index-1][pattern_index-1]
                elif pattern_char == '*':
                    if match[str_index-1][pattern_index] \
                       or match[str_index][pattern_index-1]:
                        match[str_index][pattern_index] = True

        return match[-1][-1]
