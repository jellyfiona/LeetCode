"""
1239. Maximum Length of a Concatenated String with Unique Characters_M

https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

#################################
考点或思路:
[solution: backtracking]
Similar problems:
22. Generate Parentheses : https://leetcode.com/problems/generate-parentheses/

"""

from typing  import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        time: 06222022 
        [Approach][backgtracking]For each element in the array, it may contains no duplicate letter or may have duplicate letter.
        this is one thing to check. If it has no duplication, then it is valid to add to the final string. 
        But still we may choose it, may not choose it. So, this is a backtracking problem.
        Time_O(N * 2^N) The entire array, we have 2^N different combinations to choose from. Each one of them needs N time recursions to built. So the time_O is (N* 2^N)
        space_O(1) For the longest string , the length is no longer than 26.
        """
        
        self.resultlen = 0
        def backtrack(i,sub):
            if len(arr) == i:
                self.resultlen = max(self.resultlen, len(set(sub)))  
                return
            
            iset = set(arr[i])
            if len(arr[i]) == len(iset):
                if not iset & set(sub) :
                    backtrack(i+1, sub+arr[i])
            backtrack(i+1,sub)
            
        backtrack(0,"")
        return self.resultlen 