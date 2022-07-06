"""
49. Group Anagrams_M

https://leetcode.com/problems/group-anagrams/
#################################
考点或思路:
[solution: array]
Similar problems:

"""

from collections import Counter
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        time: 07/06/2022 10:45-10:59
        [Approach] This is a problem involves hash.
        For each word we get in the list, we need to know the requence of each letter in it. So we can't use set.
        We need to use dict, we can sort the letter of a word, make it to be the key of the dict.And the origenal word can be part of the value.
        After iterate the list, we iterate the value of the dict.
        Time_O(N*(LlgN)) N = len(strs) L=max(len(strs[i]))
        """
        wordDict = {}
        for w in strs:
            wlst = list(w)
            wlst.sort()
            tlst = tuple(wlst)
            if tlst in wordDict:
                wordDict[tlst].append(w)
            else:
                wordDict[tlst] = [w]
        
        return list(wordDict.values())