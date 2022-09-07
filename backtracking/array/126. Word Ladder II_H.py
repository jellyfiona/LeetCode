"""
126. Word Ladder II

https://leetcode.com/problems/word-ladder-ii/

#################################
考点或思路:
[solution: backtracking]
Similar problems:

22. Generate Parentheses : https://leetcode.com/problems/generate-parentheses/
1239. Maximum Length of a Concatenated String with Unique Characters_M : https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
139. Word Break_M :https://leetcode.com/problems/word-break/
79. Word Search_M : https://leetcode.com/problems/word-search/

"""

from typing import List

class Solution:
    def findLadder_TLE(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        time: 08/13/2022  7:40--8:39
        [Approach] First, from the question itself, and the example 1, we can see, there are more than one answers for the question.
        So it should not be a DP problem, it should be a backtracking problem.
        For each word, we consider it as a spot, the next word which differs by a single letter, is the neighber of the word.
        If we can make a path from beginword to endword, the path is what we want, is the valid answer.
        
        [Backtracking] this is a DFS , so time limit exceeded!!!
        """
        if endWord not in wordList:
            return []
        
        def neighber(w1:str, w2:str)->bool:
            differ = 0 
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    differ += 1
                if differ > 1:
                    return False
            return True if differ == 1 else False
        
        self.shortest = len(wordList) + 1
        output = []
        
        def backtracking(path,remainlst):
            
            if len(path) > self.shortest:
                return
            
            if path and path[-1] == endWord:
                if len(path) < self.shortest:                    
                    self.shortest = len(path)
                    output.clear()
                output.append(path.copy())
                return
            
            for i  in range(len(remainlst)):
                if neighber(remainlst[i] , path[-1]):
                    path.append(remainlst[i])
                    backtracking(path, remainlst[:i]+remainlst[i+1:])
                    path.pop()
                    
        p = [beginWord]
        backtracking(p, wordList)
        return output
        