
"""
127. Word Ladder
https://leetcode.com/problems/word-ladder/

#################################
考点或思路:
[solution][Gragh][BFS][deque]
Similar problems:
126. Word Ladder II 
"""

import queue
import string
from typing import List

from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        time: 08/13/2022 
        [Approach][万门Day21-10]
        这个是根据万门老师的代码学的，其实整个解题思路会了，但是具体的操作，比如怎么用Deque，怎么BFS的，都还是不会。
        BFS的模板：

        """
        if endWord not in wordList:
            return 0

        # 转化成set比较好找，并且题目给出了所有word都唯一，那么set转化不会丢失任何信息
        wordsSet = set(wordList)
        # beginWord may not be in the list, so we add it.
        wordsSet.add(beginWord)

        # each element in the queue, is [word, the len of the path from beginword to curword]
        queue = deque( [ [beginWord,1],  ]  )

        while queue:
            word, length = queue.popleft()
            # 如果curword 等于endword，那么就是找到了，那么就返回长度
            if word == endWord:
                return length
            #没找到的话，继续，
            # 对于curword，转化它的任何一个字母，如果转化之后的nextword在set中，那么就是找到了
            # 那么就把这一level的word和步长加入到queue中。
            # 这样的话，同一步长的所有word都一起加入到queue，排队等到他们再顺序处理。，
            # 那么最后找到了endword的时候，就肯定是最短的了。因为他们排队等待的时候，就是按照距离排队的。
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    next_word = word[i:] + c + word[i+1:]
                    if next_word in wordsSet:
                        wordsSet.remove(next_word)
                        queue.append([next_word, length+1])
        return 0