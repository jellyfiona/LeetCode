
"""
1642. Furthest Building You Can Reach_M

https://leetcode.com/problems/furthest-building-you-can-reach/

##############################

Similar problems:

#################################
考点或思路:
[solution1: binarySearch]
[solution2:heapq]
"""
from typing import List
import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        time: 06212022 10:25--11:30
        [Approach] according to the description of this question, the ladder can be as long as it need to be,
        we should use bricks for shorter climbs, ladder for longer climbs.
        [binarySearch] I have not came up with a better solution. This is easy to understand. I get a midpoint, 
        I look up if I can reach this midpoint, if yes, left point go bigger; if not, right point go smaller.
        How to check if I can reach a midpoint? I go through the array from idx=0 to midpoint, gather the deltas,
        sort them, use ladders for the longest delta, for the rest of delta, check if bricks is enough.
        [二分] 没想到更好的方法，试一下这个，先二分，然后看看是否可以达到，能达到就再往右，再二分，最后到达能到的地方。
        但是二分的每一轮中，都要对当前整个考虑范围内的高度遍历，list出全部delta， 然后再排序，再遍历排序，从小到大，用掉brick和ladder，
        看能不能走到当前这个mid位置。
        time_O(N) N=(logN * (N+NlogN)) 
        space_O(1) 
        """
        
        def CanGo(p):
            d = []
            for i in range(1,p+1):
                if heights[i]>heights[i-1]:
                    d.append(heights[i]- heights[i-1])
            d.sort()
            if len(d) <= ladders:
                return True
            elif sum(d[:len(d)-ladders]) <= bricks:
                return True
            else:
                return False

        left = 0
        right = len(heights) -1
        while left < right:
            mid = left + (right - left + 1) // 2
            if CanGo(mid):
                left = mid
            else:
                right =  mid - 1
                
        return left

    
    def furthestBuilding_V1(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        [Approach2] as we go forther with the array, we will see more climbs on the way, we should but ladders to the longest climbs
        so far we have seen, and others with bricks. till we have no ladders or bricks.
        when we see a new climb with a delta greater than any other delta we have seen before, we find the last longest climb with ladders, and check if this ladder can be replaced with bricks, if can ,we replace it, we put the ladder to the new greatest delta.
        If we can replace it, then we can not go forther.
        And as we may see greater and greater climbs, the ladder we stored need to change all the time meanwhile we need to sort them.
        so we should use heapq. 
        the ladders we have placed are the cadidate pool that we may need choose from, we choose the shortest ladder.
        time_O(N)
        space_O(N) need extra space storing where the ladders were put and how many bricks it needs to replace.
        """
        
        laddersheap = []
        for i in range(1, len(heights)):
            if heights[i] > heights[i-1]:
                if len(laddersheap) < ladders:
                    heapq.heappush(laddersheap,heights[i] - heights[i-1])
                elif laddersheap and (heights[i] - heights[i-1]) > laddersheap[0] and bricks >= laddersheap[0]:
                    bricks -= laddersheap[0]
                    heapq.heappushpop(laddersheap,heights[i] - heights[i-1])
                elif bricks >= heights[i] - heights[i-1]:
                    bricks -= (heights[i] - heights[i-1])
                else:
                    return i-1
        return len(heights)-1