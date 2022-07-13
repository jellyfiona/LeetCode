"""
54. Spiral Matrix_M

https://leetcode.com/problems/spiral-matrix/
#################################
考点或思路:
[solution: Matrix]  math & logic
Similar problems:

"""


from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        time: 07/13/2022 10:40---11:12 还要debug，不debug还写不出来
        [Approach] [math] we set a range for row and a range for col, and we prepare 4 directions to turn.
        we start traverse the matrix from (0,0) and go right first, when we hit the right border we turn to next direction which is down.
        time_O(N)
        space_O(1)
        """
        # left, right, up, down
        cur_b = [0, len(matrix[0]) -1, 0 , len(matrix) - 1]
        
        dirs = [(0,1), (1,0), (0,-1),(-1,0)]
        di = 0 # first, we go right
        borderChanges = [(0,0,1,0),(0,-1,0,0),(0,0,0,-1),(1,0,0,0)]
        cur_r = 0
        cur_c = 0
        res = [matrix[cur_r][cur_c],] # the output
        
        while cur_b[0] <= cur_b[1] and cur_b[2] <= cur_b[3]:
            
            while cur_b[0] <= cur_c+dirs[di][1] <= cur_b[1] and cur_b[2] <= cur_r+dirs[di][0] <= cur_b[3]:
                cur_r += dirs[di][0]
                cur_c += dirs[di][1]
                res.append(matrix[cur_r][cur_c])
                
            cur_b = list( map(lambda i: cur_b[i] + borderChanges[di][i], range(4)))
            di = (di + 1) % 4
            
        return res
            
        
        