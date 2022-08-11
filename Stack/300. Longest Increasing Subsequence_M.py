
"""
300. Longest Increasing Subsequence_M
https://leetcode.com/problems/longest-increasing-subsequence/

##############################

类似题型:


#################################
考点或思路:

"""
from typing import List
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        time:08/08/2022  10:00--11:00
        [Approach][stack] for this problem , stack can help us.
        We keep a stack of strictly increasing numbers which comes from the array nums.
        When we go through the array nums, for each number we see, we compare it with the last elment in stack.
        If new num is bigger than stack[-1] or stack is empty, we push new num into the stack;
        if new num is smaller or equel to stack[-1], [Notice***]we are NOT pop things out till we get a smaller one.
        we put the new number into stack, replace a existing number with the new one. So that,if  later we get a longer sequence,
        the longer sequence will replace and out longer the current one;
        if later we do not get longer sqeuence, the current len of stack, will be what we need.
        
        
        time_O(N) we go through the array once.
        space_O(N) we may need N space for stack.
        """
        stack = []
        
        for n in nums:
            if stack == [] or stack[-1] < n:
                stack.append(n)
            else:
                # find the element to be replaced 
                idx = bisect.bisect_left(stack,n)
                stack[idx] = n
            
        return len(stack)