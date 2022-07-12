"""
473. Matchsticks to Square_M
https://leetcode.com/problems/matchsticks-to-square/

#################################
考点或思路:
[solution: backtracking+cache]
Similar problems:
22. Generate Parentheses : https://leetcode.com/problems/generate-parentheses/
1239. Maximum Length of a Concatenated String with Unique Characters_M : https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
139. Word Break_M :https://leetcode.com/problems/word-break/

"""

from typing import List
from functools import lru_cache
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        time: 07/12/2022
        [Approach][backtracking+cache] I feel this is a math problem.
        For it works, the sum of the array is the peramoter of the square, and we can divide the sum by 4 to get the side.
        We should be able to find 4 set of the elements, and the sum of each set equels to the side of the square.
        time_O(4^N)
        space_O(N) recursion for N time, so space_O(N)
        """
        p = sum(matchsticks)
        side = p // 4
        # the array is an integer array, so the side must be int.
        if side * 4 != p:
            return False
        
        s = [0] * 4
        
        matchsticks.sort(reverse=True)
        if matchsticks[0] > side:
            return False
        
        @lru_cache(None)
        def backtracking(i,tupleS):
            if i >= len(matchsticks):
                # we dont have to check th 4th side, it is asured before, that the first 3 side be the length we want, the 4th will be the same.
                return tupleS[0]==tupleS[1]==tupleS[2]==side

            
            lstS = list(tupleS)
            for j in range(4):
                lstS[j] += matchsticks[i]
                if lstS[j] <= side:
                    if backtracking(i+1,tuple(lstS)):
                        return True
                lstS[j] -= matchsticks[i]
            return False
        
        return backtracking(0,tuple(s))