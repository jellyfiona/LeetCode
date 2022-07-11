"""
135. Candy

https://leetcode.com/problems/candy/
#################################
考点或思路:
[solution: greedy]
Similar problems:
42. Trapping Rain Water_H

"""
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        time: 07/04/2022
        前边做了一个多小时，怎么改算法都是错的，55555】
        后边就看了solution，而且因为看到这个题是贪心算法的题，自己知道自己对贪心算法根本不了解.....
        所以还是来学别人的解法吧。
        【解1，双向状态方程】这个跟trapping rain water解法一样。用我起名叫双向状态方程的方法。
从左往右，如果ratings[i]< ratings[i-1],那么candy[i]=candy[i-1]+1，否则就跟前边得糖一样多，这样得到一个list；再从右向左来一遍。然后两个list对应位置取max值，得到的就是这个小孩应该得糖的list。
        time_O(N）
        space_O(N)
        """
        childrenCnt = len(ratings)
        l2r = [1] * childrenCnt
        r2l = [1] * childrenCnt
        
        for i in range(1,childrenCnt):
            if ratings[i] > ratings[i-1]:
                l2r[i] = l2r[i-1] + 1
            
        for i in range(childrenCnt-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                r2l[i] = r2l[i+1] + 1
                
        ret = sum(map(max, [(l2r[i],r2l[i]) for i in range(childrenCnt) ]))
        return ret