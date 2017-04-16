class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagrams_dict:
                anagrams_dict[sorted_word] = [word]
            else:
                anagrams_dict[sorted_word].append(word)

        ans = [anagrams for anagrams in anagrams_dict.values()]
        return ans
