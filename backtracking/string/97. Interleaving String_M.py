
"""
97. Interleaving String_M

https://leetcode.com/problems/interleaving-string/
#################################
考点或思路:
[solution:]
[backtracking + lru_cache][two pointers]
Similar problems:
526. Beautiful Arrangement_M
139. Word Break_M
140. Word Break II_H
1155. Number of Dice Rolls With Target Sum_M
22

"""

from typing import List


from functools import lru_cache
class Solution:
    @lru_cache(None)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        time: 07/07/2022   10:55--11:35
        [Approach] [Two pointers][backtrack+ lru_cache]
        For this problem, I will set one pointers for each of the strs.
        We iterate the s3, and compaire the element with the current pointer of s1(p1) and the current pointer of s2 (p2).
        if s3[i] == p1, then p1 move one step forward, else if s2[i] == p2, then p2 move one step forward.
        else, it means the s3[i] can not be found in neither s1 nor s2 accordingly, so we return False.
        There is one thing we need to be careful. If P1==P2 , which one should we choose to move forward?
        I think we have to use backtracking, or say, we have to try both, to see either one of them may be the solution.
        Time_O(N!) N = len(s3)
        space_O(1)
        """
        len1 = len(s1)
        len2= len(s2)
        idx1 = 0
        idx2 = 0
        
        if len1+len2 != len(s3):
            return False
        
        for i in range(len(s3)):
            if idx1< len1 and idx2< len2 and s1[idx1]== s2[idx2]== s3[i]:
                r1 = self.isInterleave(s1[idx1+1:] , s2[idx2:], s3[i+1:])
                r2 = self.isInterleave(s1[idx1:] , s2[idx2+1:], s3[i+1:])
                return r1 or r2
            elif idx1< len1 and s3[i] == s1[idx1]:
                idx1 += 1
            elif idx2 < len2 and s3[i] == s2[idx2]:
                idx2 += 1
        
            else:
                return False
        return True
                    
        
        