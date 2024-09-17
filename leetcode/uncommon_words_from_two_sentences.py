# https://leetcode.com/problems/uncommon-words-from-two-sentences

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = {}
        uncommons = []

        for word in s1.split() + s2.split():
            words[word] = words.get(word, 0) + 1
        for word, count in words.items():
            if count == 1:
                uncommons.append(word)
        return uncommons
