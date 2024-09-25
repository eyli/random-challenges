# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_tree = PrefixTreeNode()
        for word in words:
            cur_node = prefix_tree
            for c in word:
                if c not in cur_node.children:
                    cur_node.children[c] = PrefixTreeNode()
                cur_node = cur_node.children[c]
                cur_node.val += 1

        output = []
        for word in words:
            cur_node = prefix_tree
            score = 0
            for c in word:
                next_node = cur_node.children[c]
                score += next_node.val
                cur_node = next_node
            output.append(score)
        return output


class PrefixTreeNode:
    def __init__(self):
        self.val = 0
        self.children = {}
