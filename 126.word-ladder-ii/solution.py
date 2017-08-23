import string
from collections import defaultdict


class Solution(object):
    def get_all_paths(self, graph, begin, end):
        # print("Constructing {} -> {}".format(begin, end))
        if begin == end:
            return [[end]]

        if begin not in graph:
            return None

        ans = []
        for word in graph[begin]:
            sub_ans = self.get_all_paths(graph, word, end)
            if not sub_ans:
                continue

            for one in sub_ans:
                one.insert(0, begin)
            ans.extend(sub_ans)

        return ans

    def create_next_level_graph(self, word, word_set, graph, next_level_set):
        for i in range(len(word)):
            for ch in string.ascii_lowercase:
                if ch == word[i]:
                    continue
                new_word = word[:i] + ch + word[i+1:]
                if new_word in word_set:
                    graph[word].add(new_word)
                    next_level_set.add(new_word)

    def create_graph(self, beginWord, endWord, word_set):
        graph = defaultdict(set)
        current_level_set = set([beginWord])
        while current_level_set:
            next_level_set = set()
            word_set.difference_update(current_level_set)
            for current in current_level_set:
                # print("Queue: {}".format(current_level_set))

                self.create_next_level_graph(current, word_set, graph, next_level_set)

            if endWord in next_level_set:
                break
            current_level_set = next_level_set
            # print("")

        return graph

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        graph = self.create_graph(beginWord, endWord, word_set)

        # print("Graph: {}".format(graph))
        ans = []
        if graph:
            ans = self.get_all_paths(graph, beginWord, endWord)
        return ans
