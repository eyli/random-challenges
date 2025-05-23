# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        self._insertHelper(self.root, word)

    def _insertHelper(self, node, word):
        if not word:
            node['EOW'] = True
            return

        if word[0] not in node:
            next_node = {}
            node[word[0]] = next_node
        else:
            next_node = node[word[0]]
        self._insertHelper(next_node, word[1:])


    def search(self, word: str) -> bool:
        current_node = self.root
        for c in word:
            if c not in current_node:
                return False
            else:
                current_node = current_node[c]
        return 'EOW' in current_node

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for c in prefix:
            if c not in current_node:
                return False
            else:
                current_node = current_node[c]
        return True
