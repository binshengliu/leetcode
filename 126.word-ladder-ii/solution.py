class Solution(object):
    def isOneCharDiff(self, word1, word2):
        oneCharDiff = False
        for (a, b) in zip(word1, word2):
            if a == b:
                continue

            # a != b
            if oneCharDiff:
                return False
            else:
                oneCharDiff = True

        return oneCharDiff

    def getAllPaths(self, graph, begin, end):
        # print("Constructing {} -> {}".format(begin, end))
        if begin == end:
            return [[end]]

        if begin not in graph:
            return None

        ans = []
        for word in graph[begin]:
            sub_ans = self.getAllPaths(graph, word, end)
            if not sub_ans:
                continue

            for one in sub_ans:
                one.insert(0, begin)
            ans.extend(sub_ans)

        return ans

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        graph = {}
        bfsSet = set([beginWord])
        while bfsSet:
            nextLevelQueue = set()
            wordSet.difference_update(bfsSet)
            for current in bfsSet:
                # print("Queue: {}".format(bfsSet))
                if current == endWord:
                    break

                for word in wordSet:
                    if self.isOneCharDiff(current, word):
                        # print("key: {}, value: {}".format(current, word))
                        graph.setdefault(current, []).append(word)
                        nextLevelQueue.add(word)

            bfsSet = nextLevelQueue
            # print("")

        # print("Graph: {}".format(graph))
        ans = []
        if graph:
            ans = self.getAllPaths(graph, beginWord, endWord)
        return ans
