"""
78. Subsets_M
https://leetcode.com/problems/subsets/

#################################
考点或思路:
[solution: backtracking]
Similar problems:
22. Generate Parentheses : https://leetcode.com/problems/generate-parentheses/
1239. Maximum Length of a Concatenated String with Unique Characters_M : https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
139. Word Break_M :https://leetcode.com/problems/word-break/
39. Combination Sum_M  https://leetcode.com/problems/combination-sum/
"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        time : 06/27/2022 
        [Approach]  This is a backtracking problem. For each element in the nums array, we either choose it or not.
        This generation of subsets can be shown as a binary tree. Each level of the tree denote for an element. 
                    []
                /           \
              []              [1]
            /    \          /      \
          []      [2]      [1]      [1,2]
         /\       / \      / \      /   \
       [] [3]  [2][2,3]  [1] [1,3] [1,2] [1,2,3]
       time_O(N * 2^N)  We have 2^N subsets, and each subset needs N steps to generate.
      space_O(N)  Dispite the space for the resaults, we need N to generation.
         """
        self.res = []
        l = len(nums)
        if l == 0:
            return self.res
        
        
        def backtracking(i,subset):
            if i >= l:
                self.res.append(subset)
                return 
            
            backtracking(i+1, subset.copy())
            
            subset.append(nums[i])
            backtracking(i+1,subset.copy())
            
            return
        
        backtracking(0,[])
        return self.res