"""
139. Word Break_M

https://leetcode.com/problems/word-break/

#################################
考点或思路:
[solution: backtracking]
Similar problems:
22. Generate Parentheses : https://leetcode.com/problems/generate-parentheses/
1239. Maximum Length of a Concatenated String with Unique Characters_M : https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
140. Word Break II_H


[solution2 : divide and conquer]
"""
from typing import List
import functools
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        time: 06/24/2022 9:34--10:00
        [Approach] The input string can be break in any position, and there may be many vaild ways to break it at the beginning.
        but may not be valid for latter substring. Each movement we make, has a lot of options, and one or more of them may be valid for a solution. That why we need backtracking. 
        time_O() ???
        space_O() 
        """
        l = len(s)
        wordSet = set(wordDict)
        @functools.lru_cache(None)
        def backtracking(idx: int):
            if idx >= l:
                return True
            
            for i in range(1,20+1):
                w = s[idx:idx+i]
                if w in wordSet and backtracking(idx+i):
                    return True
                
            return False
        
        return backtracking(0)


        def wordBreak_V1(self, s: str, wordDict: List[str]) -> List[str]:
        """
        [Approach][divide and conquer] For a valid solution, there are muiltiple break point in the input string.
        Each of the break point apart the string into two substring which also are valid to break apart and be in the wordDict.
        **674 ms, faster than 5.17% of Python3 online submissions for Word Break.**

        time_O() ???
        """
    
        wordset = set(wordDict)
        @functools.lru_cache(None)
        def backtracking(subs):
            if subs in wordset:
                return True
            
            for bp in range(1,len(subs)):
                first = subs[:bp]
                second = subs[bp:]
                if backtracking(first) and backtracking(second):
                    return True
            return False
        
        return backtracking(s)