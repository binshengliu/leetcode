import string
from collections import defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        levels = self.get_shortest_path_len(beginWord, endWord, word_set)
        return levels

    def create_next_level_graph(self, word, word_set, graph, next_level_set):
        for i in range(len(word)):
            for ch in string.ascii_lowercase:
                if ch == word[i]:
                    continue
                new_word = word[:i] + ch + word[i+1:]
                if new_word in word_set:
                    graph[word].add(new_word)
                    next_level_set.add(new_word)

    def get_shortest_path_len(self, beginWord, endWord, word_set):
        graph = defaultdict(set)
        current_level_set = set([beginWord])
        levels = 1
        found = False
        while current_level_set:
            levels += 1
            next_level_set = set()
            word_set.difference_update(current_level_set)
            for current in current_level_set:
                # print("Queue: {}".format(current_level_set))

                self.create_next_level_graph(current, word_set, graph, next_level_set)

            if endWord in next_level_set:
                found = True
                break
            current_level_set = next_level_set
            # print("")

        if not found:
            return 0

        return levels
