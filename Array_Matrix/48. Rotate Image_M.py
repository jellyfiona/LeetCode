"""
48. Rotate Image_M

https://leetcode.com/problems/rotate-image/
#################################
考点或思路:
[solution: Matrix]  math & logic
Similar problems:

"""

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        [Approach] From the example, we can tell that each grid(ri,ci) should come to grid(ci,R-1-ri) 
        where R = len(matrix), 
        time_O(R*R//2)
        space_O(1)
        """
        
        R = len(matrix)
        for i in range((R+1)//2):
            for j in range(R//2):
                # store the 1st grid
                tmp = matrix[i][j]
                cur_r = i
                cur_c = j          
                for k in range(3):
                    matrix[cur_r][cur_c] = matrix[R-1-cur_c][cur_r]
                    cur_r, cur_c = R-1-cur_c, cur_r
                     
                matrix[cur_r][cur_c] = tmp