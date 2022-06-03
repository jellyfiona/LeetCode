"""
304. Range Sum Query 2D - Immutable

https://leetcode.com/problems/range-sum-query-2d-immutable/

##############################

类似题型:
303. Range Sum Query - Immutable_E

#################################
考点或思路:
【Matrix】【PrefixSum】
"""
from types import List

class NumMatrix:
    """
    time: 2022/06/03  02:00---2:39
    [Approach]【PrefixSum】 The function sumRegion is going to be called a lot. So we should primarily focusing on the efficency of this function.
    we can calculate the sum at the inital part, it will only happen once.
    we make a matrix with the same size, each of element denote the sum of the rectangle which has the (i,j) as lower right corner and (0,0) as the upper left corner.
    So when we call sumRegion, we use the sum of four rectangles, to make up what we need.
    """

    def __init__(self, matrix: List[List[int]]):
        # time_O(N) we go though the matrix once
        self.sm = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        self.sm[0] = [ sum(matrix[0][:j+1]) for j in range(len(matrix[0]))]
        for i in range(1,len(matrix)):
            self.sm[i][0] = self.sm[i-1][0] + matrix[i][0]
            for j in range(1,len(matrix[0])):
                self.sm[i][j] =  self.sm[i-1][j] + sum(matrix[i][:j+1]) 
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 > 0  and col1 > 0:
            return self.sm[row2][col2] - self.sm[row2][col1-1] - self.sm[row1-1][col2] + self.sm[row1-1][col1-1]
        elif row1 > 0 and col1 == 0:
            return self.sm[row2][col2] - self.sm[row1-1][col2]
        elif  row1 == 0 and col1 > 0:
            return self.sm[row2][col2] - self.sm[row2][col1-1]
        else:
            return self.sm[row2][col2]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)