
"""
128. Longest Consecutive Sequence_M

https://leetcode.com/problems/longest-consecutive-sequence/
#################################
考点或思路:
[solution: Hash]

"""


from typing import List
class Solution:
    def longestConsecutive_V1(self, nums: List[int]) -> int:
        """
        time: 07/05/2022
        [Approach] This is a request that we have to write a algorithm in O(N) time.
        So, sorting the array would not be a choice.
        Then what can be O(N) algorithm? Hash, iteration. So we think in that direction.
        We can first use a dict to store the nums, so when we look up something, wo need O(1).
        Then we iterate the key of the dict. and we expend the range of the consecutive sequence.
        【注意】其实这里用dict反而麻烦了，用set更简单
        """
        numsDict = {}
        # the value of each key: true means not seen yet, false means you saw it before.
        # time_O(N)
        for n in nums:
            numsDict[n] = True
            
        longest = 0
        
        # in this part, each key gets only once accesse, so time_O(N)
        for key in numsDict.keys():
            if numsDict[key] == False:
                continue
            left = key
            right = key
            curLen = 1
            while True:
                if left - 1 in numsDict:
                    numsDict[left-1] = False
                    left -= 1
                    curLen += 1
                elif right +1 in numsDict:
                    numsDict[right+1] = False
                    right += 1
                    curLen += 1
                else:
                    longest = max(longest, curLen)
                    break
                    
        return longest  
        


    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [approach_2] same algorithm, but use set instead of dict. should be faster than dict.
        """
        
        if len(nums) == 0:
            return 0
        
        numsSet = set(nums)
        longest = 0

        for i in numsSet:
            # for each i we see, we first find the left most element in the consecutive seqeunce that contains i，
            # then we start from the left most element and expend to the right
            # 对于每个i，我们先找到包含它的连续数串中，最小的那个数字，然后从这个本段数串的最小数字一点点往右找
            if i-1 not in numsSet:
                curNum = i
                curLen = 1
                while curNum+1 in numsSet:
                    curLen += 1
                    curNum += 1
                longest = max(longest, curLen)
                
        return longest