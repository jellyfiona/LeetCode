"""
1220. Count Vowels Permutation_H

https://leetcode.com/problems/count-vowels-permutation/

题目给你一些规则，比如每个字母 后边只能跟着哪些字母。让你对五个元音字母排列，最高排列长度是入参n。
1 <= n <= 2 * 10^4
Since the answer may be too large, return it modulo 10^9 + 7.

##############################

类似题型:


#################################
考点或思路:

"""


from functools import lru_cache
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        题目给了是排列，有很多限制条件的排列。一般排列组合都可以先用decisionTree的方式分析，然后用baacktracking+cache做。
        再然后，再考虑是否可以转化为DP。
        现在我就用decisitonTree和backtracking做。
        首先我的第一个root，有五个候选，也即是说我必须画五棵树。
        对于每个node，它作为lastletter，它后边可以跟什么letter，跟的letter就是子节点。这个数是个多叉树。
        按照题目规定，每个lastletter有不同的followingLetter这个要准备好，然后backtracking的时候去循环。
        """
        
        initPool = ["a","e","i","o","u"]
        followDict = { 
                        "a" :["e"],
                        "e" :["a", "i"],
                        "i" :["a", "e","o","u"],
                        "o" :["u", "i"],
                        "u" :["a"],
                     }
        
        @lru_cache(None)
        def backtracking(lastLetter,remainingLen):
            """
            lastletter: 上一个字母，
            remainingLen： lastletter后边要接多少个letter
            """
            if remainingLen == 0:
                return 1
            else:
                cnt = 0
                for a in followDict[lastLetter]:
                    cnt += backtracking(a, remainingLen-1)
                return cnt
        
        totalCnt = 0
        for ch in initPool:
            totalCnt += backtracking(ch,n-1)
        return totalCnt %(10**9 + 7)
            