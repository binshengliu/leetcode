class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # For every word, calc its length, add to current line until
        # the length exceeds maxWidth.

        ans = []
        line = []
        word_of_line = 0
        char_of_line = 0
        for word in words:
            min_space_of_line = word_of_line - 1
            if char_of_line + min_space_of_line + len(word) + 1 > maxWidth:
                # for a line, find how many spaces should be inserted,
                # then distribute them evenly.
                spaces = maxWidth - char_of_line
                space_per_word = int(spaces / (word_of_line - 1)) \
                    if word_of_line > 1 else 0
                additional_spaces = spaces - space_per_word * \
                    (word_of_line - 1)
                astr = ''
                for w in line[:-1]:
                    astr += w + ''.join([' ' for _ in range(space_per_word)])
                    if additional_spaces != 0:
                        astr += ' '
                        additional_spaces -= 1

                astr += line[-1]
                astr = astr.ljust(maxWidth)

                ans.append(astr)

                line = []
                word_of_line = 0
                char_of_line = 0

            line.append(word)
            word_of_line += 1
            char_of_line += len(word)

        if line:
            astr = ' '.join(line)
            astr = astr.ljust(maxWidth)
            ans.append(astr)

        return ans
