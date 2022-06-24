"""
140. Word Break II_H
https://leetcode.com/problems/word-break-ii/

#################################
考点或思路:
[solution: backtracking]
Similar problems:
22. Generate Parentheses : https://leetcode.com/problems/generate-parentheses/
1239. Maximum Length of a Concatenated String with Unique Characters_M : https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
139. Word Break_M :https://leetcode.com/problems/word-break/

"""
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        [Approach] This is similar to Q139.
        So we could use backtracking.
        """
        self.res = []
        l = len(s)
        wordset = set(wordDict)
        
        def backtracking(idx, seglst):
            if idx >= l:
                self.res.append( " ".join(seglst))
                return
            
            for i in range(1,10+1):
                if idx+i >l:
                    break
                seg = s[idx:idx+i]
                if seg in wordset:
                    seglst.append(seg)
                    backtracking(idx+i,seglst)
                    seglst.pop()
                    
            return
        
        backtracking(0,[])
        return self.res