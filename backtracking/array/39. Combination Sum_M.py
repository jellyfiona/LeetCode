"""
39. Combination Sum_M
https://leetcode.com/problems/combination-sum/

#################################
考点或思路:
[solution: backtracking]
Similar problems:
22. Generate Parentheses : https://leetcode.com/problems/generate-parentheses/
1239. Maximum Length of a Concatenated String with Unique Characters_M : https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
139. Word Break_M :https://leetcode.com/problems/word-break/
78. Subsets_M  https://leetcode.com/problems/subsets/
"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time: 06/30/2022 
        [Approach] First we need to sort the candidates.
        This is backtracking problem. For each Candidate,
        we have multiply choices from not choose to choose for target//caindidate times.
        So the generation of sulition can be built as a tree structure. 
        Each level is one choice and we have N=len(candidates) choices.
        The maximum level is F = target//min(candidates).
        So,  we have N^F combinations of the candidates, as we generate we cut of those combinations that does not sum to target.
        Time_O(F * N^F) N = len(candidates) F = target//min(candidates) we have N^F combinations and each combination need F steps at most to generate.
        
        """
        candidates.sort()
        self.res = []
        l = len(candidates)
        def backtracking(tar, i, comb):
            if tar == 0:
                self.res.append(comb)    
                return 
            elif i >= l :
                return 
            elif tar < candidates[i]:
                return 
             
            frq = tar//candidates[i]
            for f in range(frq+1):
                backtracking(tar - candidates[i]*f, i+1, comb + [candidates[i]] *f) 
                
            
        backtracking(target,0,[])
        return self.res