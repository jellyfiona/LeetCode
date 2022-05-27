"""
1405. Longest Happy String_M

https://leetcode.com/problems/longest-happy-string/

##############################

类似题型:


#################################
考点或思路:

"""
import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        [Approach] This question involves a lot of choices, like which char we can choose to be the next to attach to happystring.
        And how many we could add. With the cnt of char changes we need to resort them, so heap would be vary helpful.
        time_O(A+B+C) 
        """
        heap = []
        heapq.heappush(heap,(-a,"a"))
        heapq.heappush(heap,(-b,"b"))
        heapq.heappush(heap,(-c,"c"))
        
        happy = ""
        preCh = ""
        preCnt = 0
        while heap:
            cnt, ch = heapq.heappop(heap)
            cnt = -cnt
            if cnt >= 2 and cnt >= preCnt:
                happy += ch *2
                cnt -= 2
            elif cnt > 0:
                happy += ch
                cnt -= 1
            else:
                break
            
            if preCnt :
                heapq.heappush(heap, (-preCnt,preCh))
            preCh = ch
            preCnt = cnt
        return happy