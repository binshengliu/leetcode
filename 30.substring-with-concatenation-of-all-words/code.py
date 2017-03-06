class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # exceptions
        # ...

        counts = {}
        for w in words:
            counts[w] = counts.get(w, 0) + 1

        ans = []

        word_len = len(words[0])
        expected_len = word_len * len(words)

        for (begin, _) in enumerate(s):
            if begin + expected_len > len(s):
                break

            found = {}
            i = begin
            tmp_str = s[i:i+word_len]
            while (i < begin + expected_len) and (tmp_str in counts):
                found[tmp_str] = found.get(tmp_str, 0) + 1
                if found[tmp_str] > counts[tmp_str]:
                    break
                i += word_len
                tmp_str = s[i:i+word_len]

            # all are found
            if (i - begin) == expected_len:
                ans.append(begin)

        return ans
