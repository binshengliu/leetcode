class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        previous_length = 0
        length = 0
        for char in s:
            if char != ' ':
                length += 1
            elif char == ' ':
                previous_length = length if length != 0 else previous_length
                length = 0

        if length == 0:
            length = previous_length

        return length
