
"""
208. Implement Trie (Prefix Tree)

https://leetcode.com/problems/implement-trie-prefix-tree/

#################################
考点或思路:
[solution: ]
Similar problems:

【Trie：prefixTree】
208. Implement Trie (Prefix Tree) 基本原理，学习实现一个trie



"""

from typing import Tuple


class Trie:

    def __init__(self):
        self.children = {}
        self.isWord = False
        

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()

            cur = cur.children[c]

        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)