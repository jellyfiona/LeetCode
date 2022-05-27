"""
1647. Minimum Deletions to Make Character Frequencies Unique_M

https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

##############################

类似题型:


#################################
考点或思路:

"""

from collections import Counter
import heapq
class Solution:
    def minDeletions(self, s: str) -> int:
        """
        time: 052622/ 10:40---11:13
        [Approach] When it comse to frequency, the first thing we think , is Counter. O(N)
                    In the Counter ,wo get to know if there a chars with same frequencies. 
                    Then we work from there.
                    We could sort the values of Counter in a heap in decreasing order, O(log26) at worst
                    We go through the list from biggest to smallest, to check and to delete.O(26log26)
                    time_O(N)
                    spaece_O(1)
        """
        
        c = Counter(s)
        heap = list(map(lambda x:x*(-1), c.values()))
        heapq.heapify(heap)
        out = []
        total = 0
        while heap :
            # this is the first time frequency "maxcnt" showed
            maxcnt = heapq.heappop(heap)
            curdelete = 1
            # here is the "more than once" frequency occers and we delete to make it unique.
            while heap and heap[0] == maxcnt:
                cur = heapq.heappop(heap)
                cur += curdelete
                total += curdelete
                # if frequency bacome 0, we ignore them
                if cur < 0:    
                    heapq.heappush(heap, cur)
                    curdelete += 1
                
        return total
        