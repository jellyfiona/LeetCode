"""
17. Letter Combinations of a Phone Number_M

https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#################################
考点或思路:
[solution: backtracking]
Similar problems:
22. Generate Parentheses : https://leetcode.com/problems/generate-parentheses/

"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        time: 06/27/2022 10:05
        [Approach] Clearly we could build all the solution using a structure of tree.
        from the root, each level repersents what a digit might be.
        There are muiltipy solutions， and all the solutions can be generated as a tree structure.
        
        This kind of problem should use backtracking to solve.
        time_O(N * 4^N) N= len(digits) we need N steps to biuld a valid solution, and we have 4^N at most vaild solutions.
        space_O(4^N) we have 4^N soltions at most that we need to store them all.
        """
        digitdict = { "2": ["a","b","c"],
                      "3": ["d","e","f"],
                      "4": ["g","h","i"],
                       "5": ["j","k","l"],
                      "6": ["m","n","o"],
                       "7": ["p","q","r","s"],
                       "8" : ["t","u","v"],
                       "9" : ["w","x","y","z"]}
        self.res = []
        l = len(digits)
        def backtracking(i, prefix):
            if i >= l:
                self.res.append(prefix)
                return
            
            chlst = digitdict[digits[i]]
            for ch in chlst:
                backtracking(i+1,prefix+ch)
                
        if digits != "":
            backtracking(0,"")
        return self.res
    

    def letterCombinations_V1(self, digits: str) -> List[str]:
        """
        [Approach 2] we can build our solutions as permutation.
        Starting by "" as prefix, for each digits we visit, we have 3~4 choice, we attach the new choices to the end of the prefix,
        we get new prefixlst for next digits.
        time_O(4^N) The generation takes N steps, and each step we nedd to for loop for 4 time at most.
        space_O(4^N) for storage of the resualt.
        """
        if digits == "":
            return []
        
        digitdict = { "2": ["a","b","c"],
                      "3": ["d","e","f"],
                      "4": ["g","h","i"],
                       "5": ["j","k","l"],
                      "6": ["m","n","o"],
                       "7": ["p","q","r","s"],
                       "8" : ["t","u","v"],
                       "9" : ["w","x","y","z"]}
        res = [""]

        for nu in digits:
            prefixlst = res
            newlst = []
            for ch in digitdict[nu]:
                newlst += list( map(lambda x:x +ch, prefixlst)  )
            res = newlst
        return res
            
            