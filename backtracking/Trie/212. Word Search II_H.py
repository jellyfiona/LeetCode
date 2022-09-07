
"""
212. Word Search II
https://leetcode.com/problems/word-search-ii/


#################################
考点或思路:
[solution: backtracking]
Similar problems:
下边这些都是backtracking，但是不是trie
22. Generate Parentheses : https://leetcode.com/problems/generate-parentheses/
1239. Maximum Length of a Concatenated String with Unique Characters_M : https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
139. Word Break_M :https://leetcode.com/problems/word-break/
79. Word Search_M : https://leetcode.com/problems/word-search/


【Trie：prefixTree】
208. Implement Trie (Prefix Tree) 基本原理，学习实现一个trie

"""

from typing import List

""" 这个题的关键，是使用trie，即prefixTree，这个prefixTree， 其实是个Narry-Tree。有N个childnode。
    首先有一个root，这个不包含任何前缀，是前缀的起始点。它下边是所有一个字母的前缀的node，
    每个level的node，就是前缀的单词在第几位置的字母。
    每个node有自己的val，即字母，还有children，还有标识自己当前是否是一个单词的结尾字母。这个是为了方便我们在search的时候，判定我们是否还要继续递归的找。
    本题首先我们要定义一个trie。才能继续进行。题目本身没有给，就是考察我们，看我们知不知道要自己实现一个trie。
"""
class TrieNode:
    def __init__(self,letter) -> None:
        # 定义child的时候，你也可以用list，但是list在查找是否有某个后续字母的时候，不方便，所以更好的实现是用hashmap。
        # 这样每个key，就是下一个字母，value就是具体的node
        self.children = {}
        self.letter = letter
        # 默认设置为不是词语，还只是前缀
        self.isWord = False

    def _addChild(self,node : "TrieNode"):
        self.children[node.letter] = node


    def addword(self, word):
        # 把 word 添加到当前树下
        cur = self
        for c in word:
            if c not in self.children:
                self.children[c] = TrieNode(c)
        
            cur = self.children[c]

        cur.isWord = True
        return cur

    def search(self,word):
        cur = self
        for c in word:
            if c not in self.children:
                return False
            cur = self.children[c]

        return cur.isWord

    def startwith(self, prefix):
        cur = self
        for c in prefix:
            if c not in self.children:
                return False
            cur = self.children[c]
        return not cur.isWord

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # step one: build prefix tree
        root = TrieNode("")
        for w in words:
            root.addword(w)

        rows , cols = len(board), len(board[0])
        outputSet, visitedSet = set(), set()

        def rec(r,c, node, substr):
            # r,c is where are we now on the board, the next ch we with check
            # node is the current Trienode we are on, it may be a char in a prefix path
            # substr is the prefix path we just visit and build up, will become a word in the list ,
            # and when that happens, we put the substr into our outputSet.
            

        # step two: recurse to search word
        # step three: go through the board