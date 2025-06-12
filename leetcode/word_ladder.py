# https://leetcode.com/problems/word-ladder/

from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)

        wordList = list(set(wordList + [beginWord]))

        def is_adjacent(word1, word2):
            diffs = 0
            if len(word1) != len(word2):
                return False
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diffs += 1
                    if diffs > 1:
                        return False
            return True

        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                word1 = wordList[i]
                word2 = wordList[j]
                if is_adjacent(word1, word2):
                    graph[word1].append(word2)
                    graph[word2].append(word1)

        to_visit = deque([beginWord])
        distance = 0
        seen = set()
        while to_visit:
            distance += 1

            for i in range(len(to_visit)):
                word = to_visit.popleft()
                if word == endWord:
                    return distance

                adjacents = graph[word]
                for adjacent in adjacents:
                    if adjacent not in seen:
                        to_visit.append(adjacent)
                        seen.add(adjacent)
        return 0
