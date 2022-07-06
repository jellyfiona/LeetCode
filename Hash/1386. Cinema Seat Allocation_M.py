"""
1386. Cinema Seat Allocation

https://leetcode.com/problems/cinema-seat-allocation/

##############################

类似题型:

#################################
考点或思路:
[Array][Hash]
"""

from typing import List
from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """
        time: 061602002
        [Approach] It is pretty obvious that there are 3 certain patterns of 4-person groups
        [2,3,4,5][4,5,6,7][6,7,8,9].
        so we can set a table for that, for each row, if the col of reservedSeat is in the above pattern group,
        we would know that the coordinery group is not available.
        """
        left = [2,3,4,5]
        middle = [4,5,6,7]
        right = [6,7,8,9]
        
        total_seats = defaultdict(lambda :[1,1,1])
        
        for seat in reservedSeats:
            if seat[1] in left:
                total_seats[seat[0]][0] = 0
            if seat[1] in middle:
                total_seats[seat[0]][1] = 0
            if seat[1] in right:
                total_seats[seat[0]][2] = 0
        
        maxgroup = 0
        
        for r in range(n):
            nowrow = sum( total_seats[r+1])
            if nowrow >= 2:
                maxgroup += 2
            else:
                maxgroup += nowrow

        return maxgroup
            
