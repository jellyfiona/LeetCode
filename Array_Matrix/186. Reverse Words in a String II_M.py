
"""
186. Reverse Words in a String II

https://leetcode.com/problems/reverse-words-in-a-string-ii/
#################################
考点或思路:
[solution: array]
Similar problems:


"""
from typing import List
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        [Approach] First, we can apart the array into words by find the next " ",
        Then for each word we set apart, we reversce it in place. 
        After we reverse each word in-place, we reverse the entire list.
        time_O(N) we go through the array once.
        space_O(1)
        """
        
        l= len(s)
        curSpace = 0
        spaceCnt = s.count(" ")
        left = 0
        
        while curSpace < spaceCnt:
            right = s[left:].index(" ") + left
            curSpace += 1
            # reversce s[left:right]
            i = 0
            while i in range((right-left)//2):
                s[left + i], s[right-1-i] = s[right-1-i],s[left+i]
                i+=1
            
            left = right + 1
            
        # here is the last word
        right = len(s)
        i = 0
        while i in range((right-left)//2):
            s[left + i], s[right-1-i] = s[right-1-i],s[left+i]
            i+=1
       
        s.reverse()
        
        
            