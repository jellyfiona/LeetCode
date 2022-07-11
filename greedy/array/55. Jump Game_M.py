"""
55. Jump Game_M

https://leetcode.com/problems/jump-game/

#################################
考点或思路:
[solution: greedy]
Similar problems:
42. Trapping Rain Water_H

"""

from gettext import dpgettext
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        time: 07/09/2022 
        [Approach][Greedy] 这个是设定最后一个idx是我们的goal，从后往前遍历，如果前边的idx可以走到后边的goalidx甚至更往后，那么我们的goalIdx可以提前，也就是说，
        如果lastIdx -2 这里可以走到lastIdx，那么更前边的元素，只要能走到lastIdx-2 就可以了，后边一定是能走下去的。所以我们可以把goalIdx提前到lastidx-2。
        这样一段一段往前提，一直到，goelIdx提前到idx-0，为止。或者走到一个idx就无法提前了，终止了，那么说明idx-0是走不到最后的。
        time_O(N) 遍历一遍list即可，
        sapce_O(1)
        """
        
        goalIdx = len(nums) - 1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= goalIdx:
                goalIdx = i
            
        return goalIdx == 0

    def canJump_V1(self, nums: List[int]) -> bool:
        far = 0
        step = 0
        n = len(nums)
        for i in range(n):
            if i + nums[i] >= n-1:
                return True 
            far = max(far,i+nums[i])
            if i == far:
                step += 1
                far = nums[i]
            if far == 0:
                return False

        return False

    def canJump_V2(self, nums: List[int]) -> bool:
        """
        [BackTracking]
        可以递归的把每一个position上可以走的step都尝试一遍，看看哪一条可以走到最后，
        time_O(2^N)
        space_O(1)
        """

        def backtracking(pos, nums):
            if pos >= len(nums)-1:
                return True

            farest = min(len(nums) - 1, pos + nums[pos])
            for p in range(pos+1,farest+1):
                if backtracking(p, nums):
                    return True
            # if all the steps we try from this position are all fail, the we return False
            return False

        return backtracking(0,nums)
        
    def canJump_V3(self, nums: List[int]) -> bool:
        """
        [反向 DP]
        可以递归的把每一个position上可以走的step都尝试一遍，看看哪一条可以走到最后，
        time_O(2^N)
        space_O(1)
        """
        # DP[i] stands for position i can or cannot reach to the lastIdx
        DP = [False] * len(nums)
        DP[-1] = True

        # treveral from right to left, for each element, say it is on idx i, if DP[i+1: i+k+1] in this part , has at least one True, then DP[i] = Ture
        for i in range(len(nums) - 2, -1, -1):
            farest = min(len(nums)-1, nums[i]+i)
            if sum( DP[i+1:farest+1]) >= 1:
                DP[i] = True
        
        return DP[0]



import unittest
class TestcaseS(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()
        self.f = self.obj.canJump

    def testcase_1(self):
        alist = [2,3,1,1,4]
        ret = self.f(alist)
        self.assertEqual(ret,True)

        alist =  [2,3,0,1,4]
        ret = self.f(alist)
        self.assertEqual(ret,True)

        alist = [1,2,3]
        ret = self.f(alist)
        self.assertEqual(ret,True)

        alist = [1]
        ret = self.f(alist)
        self.assertEqual(ret,True)
        alist = [0]
        ret = self.f(alist)
        self.assertEqual(ret,True)

    def testcase_V1(self):
        print("*********************************************************")
        self.f = self.obj.canJump_V1
        self.testcase_1()

    def testcase_V2(self):
        print("*********************************************************")
        self.f = self.obj.canJump_V2
        self.testcase_1()        

    def testcase_V3(self):
        print("*********************************************************")
        self.f = self.obj.canJump_V3
        self.testcase_1()  

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)        