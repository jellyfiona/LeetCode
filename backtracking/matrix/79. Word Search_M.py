"""
79. Word Search_M
https://leetcode.com/problems/word-search/

#################################
考点或思路:
[solution: backtracking]
Similar problems:
22. Generate Parentheses : https://leetcode.com/problems/generate-parentheses/
1239. Maximum Length of a Concatenated String with Unique Characters_M : https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
139. Word Break_M :https://leetcode.com/problems/word-break/

"""
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        time: 06042022
        [Approach][BFS][Backtracking]
        First, we iterate the board to find the first letter in the word, start from there,
        we BFS to the neighbers of the letter to find the second letter, 
        if yes, we go deep to the third letter and so on till the word is complete and return true or we reach to a deadend 
        or we have go over the board already;
        Even if yes, this step's yes may not the finally solution, so we need to backtrack this step and continue search for 
        another second letter in first letter's neighber.
        time_O(N * 4^L) N = sizeof(board) L = len(word)
        space_O(N)        
        """
        wordlen = len(word)
        r = len(board)
        c = len(board[0])
        seen = [[False] * c for _ in range(r)]
        
        def neighbers(i,j):
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            for di in dirs:
                x = i+di[0]
                y = j+di[1]
                if 0<=x<r and 0<=y<c:
                    yield x,y
        
        
        # backtrack, here ,each level of this function has a for loop if 4(4 neighbers)
        # and the deepth is L (L = len(word))
        # so the time_O(4^L)
        def backtrack(i,j,seen,widx):
            # i,j is the cur grid we are at, widx is the cur letter of the word we are at
            if widx+1 == wordlen:
                return True
            
            for nbi, nbj in neighbers(i,j):
                if seen[nbi][nbj]:continue
                if board[nbi][nbj] == word[widx+1]:
                    seen[nbi][nbj] = True
                    if backtrack(nbi,nbj,seen,widx+1):
                        return True
                    seen[nbi][nbj] = False
                    
            return False
                    
        # time_O(N)
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    seen[i][j] = True
                    if backtrack(i,j,seen.copy(),0):
                        return True
                    seen[i][j] = False
        return False