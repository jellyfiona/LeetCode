"""
5. Longest Palindromic Substring_M

https://leetcode.com/problems/longest-palindromic-substring/
#################################
考点或思路:
[solution: String]

"""


from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        [Approach]This is a problem to find a substring , that means the answer of it is continuous.
        For each char of the string, we consider it as the center of our substr, and we extend it, to see how far each side could go.
        time_O(N^2) for each char we try, it takes N/2 at most to know the length of the palindrome there is.
        """
        lenOfS = len(s)
        def lengthOfPalindrome(i,j = None):
            if j == None:
                left = i
                right = i
            else:
                left = i
                right = j
            sub = s[i]
            while left >=0 and right < lenOfS:
                if s[left] != s[right]:
                    return sub
                else:
                    sub = s[left:right+1]
                    left -= 1
                    right += 1
            return sub
        
        
        longestSub = ""
        for i in range(lenOfS):
            sub1 = lengthOfPalindrome(i)
            sub2 = lengthOfPalindrome(i,i+1)
            if len(sub1) > len(longestSub):
                longestSub = sub1
            if len(sub2) > len(longestSub):
                longestSub = sub2

        return longestSub