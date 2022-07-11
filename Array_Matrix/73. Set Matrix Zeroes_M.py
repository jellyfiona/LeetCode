"""
73. Set Matrix Zeroes_M

https://leetcode.com/problems/set-matrix-zeroes/
#################################
考点或思路:
[solution: matrix]
Similar problems:

"""

from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #[approch_1] [time_O(M*N)]
        row = len(matrix)
        col = len(matrix[0])
        rowset = set()
        colset = set()
        
        for i in range(row):
            for j in range(col):
                if i in rowset and j in colset:
                    continue
                if matrix[i][j] == 0:
                    rowset.add(i)
                    colset.add(j)
                    
        for i in rowset:
            matrix[i] = [0] * col
                
        for j in colset:
            for k in range(row):
                matrix[k][j] = 0
                
        return 