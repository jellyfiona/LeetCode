"""
1048. Longest String Chain——M

https://leetcode.com/problems/longest-string-chain/

##############################

类似题型:


#################################
考点或思路:
[DP][logic]
"""
from typing import List
from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        time: 06152022  
        [Approach] [DP]
        后边的长word能组成多长的chain，取决于它前边的祖先已经组成了多长的chain。
        所以显然这个需要word先排个序，对于短word先处理，知道了短word能组多长的chain之后，再访问长word，对于每个长word，
        查看它的各个祖先的可能词汇，是否是我们已经访问过了的，如果在list中，那么我们肯定已经访问过了，已经知道了这个祖先词最长的chain的长度，
        那么当前这个词的最长chain，就是祖先词的chain长度+1。这样遍历过后，我们就能够知道全部的最长chain长度了。
        time_O(NlogN+N*L) N=len（words） L=max(len(each word)) 
        space_O(N) for each word, we need store their longest chain length in the dict
        """
        di=defaultdict(int) # key = words, value = length of a chain if the key is the last word of a chain
        
        # time_O(NlogN)
        words.sort(key = len)
        longest = 1        
        # now the words is sorted, we should be visiting the shorter words sooner than the longer ones.
        # time_O(N)
        for w in words:
            di[w] = 1
            # time_O(L) L is 16 at most
            for i in range(len(w)):
                pre = w[:i]+w[i+1:]
                if pre in di:
                    di[w] = max(di[w], di[pre]+1)
            longest = max(longest,di[w])
                
        return longest
                
        
                    