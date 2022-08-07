"""
377. Combination Sum IV_M

https://leetcode.com/problems/combination-sum-iv/

##############################

类似题型:


#################################
考点或思路:

"""



from typing import List
from functools import lru_cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        time: 08/05/2022 10:05---
        [Approach][backtracking][decition Tree???][top->bottum]
        If we do it top->bottum, as dicition tree,
                                       0
                /(1)                    |(2)             \(3) 
                 1                      2                 3
        /(1)   |(2)   \(3)    /(1)   |(2)   \(3)       /(1)   |(2)   \(3)  
       2       3       4(√)   3      4(√)    5(×)      4(√)   5(×)    6(×)
   /(1) |(2)\(3)
  3     4(√)  5(×)
/(1)
4(√)
 用决策树分析，可以看到，如果root是当前的sum，从0开始 ，每次加一个nums的数字，我们一层一层加下去可以得到这样一棵树。
 leaf是target的就是我们需要的path，大于target的就不能进行下去了。
 所以从这个角度，我们其实可以用backtracking的方式，得到最终的path个数。
 值得注意的是：本题中，（1,1,2,1）(1,2,1,1)都是合法的解，那么恰好让我们可以更简单的使用backtracking。
 这里可以设计backtracking的函数，使得我们可以使用cache。这样更快。
 
        """
        
        
        self.path = 0
        
        @lru_cache(None)
        def backtracking(curSum, target):
            if curSum > target:
                return 0
            elif curSum == target:
                return 1
            else:
                cnt = 0
                for i in nums:
                    s = curSum + i
                    cnt += backtracking(s,target)
                return cnt
            
        
        r = backtracking(0,target)
        return r