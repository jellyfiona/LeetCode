"""
348. Design Tic-Tac-Toe

https://leetcode.com/problems/design-tic-tac-toe/

##############################

类似题型:


#################################
考点或思路:
[OOD][logic]
"""

class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.winner = 0 # to mark winner, is to make sure once we have a winner, no movement will be made.
        
        # if we can make sure the input will always be valid, no repeated grid will be the input , we dont need to store the board.
        self.grid = [[0] * n for _ in range(n)]
        # r means each index means this row has a chance to be completed by one player.
        # for the first grid it was occupied by a player , the r[ridx] will be mark as the players id
        # if later the other player put a piece in the row , the r[idx] will be mark as False
        self.r = [[0,0] for _ in range(n)] # (players id, the number of pieces this player put on the row )
        self.c =  [[0,0] for _ in range(n)]
        self.diagonal_1 = [0,0]
        self.diagonal_2 = [0,0]
        
        
    def move(self, row: int, col: int, player: int) -> int:
        """
        [Approach] we dont check each row or each col or each diagonal every time,
        we mark them every time, so we just mark them and we just check our marks.
        All the marks we have made is n rows, n col, and 2 diagonals.
        So time_O(2N+2)---> time_O(N)
        space_O(2N+2) ---> space_O(N)
        """
        if self.winner:
            return self.winner
        
        self.grid[row][col] = player
        if self.r[row][0] == player or self.r[row][0]==0:
            self.r[row][0] = player
            self.r[row][1] += 1
            if self.r[row][1] == self.n:
                self.winner = player
                return player
        else:
            self.r[row][0] = False
        
        if self.c[col][0] == player or self.c[col][0] == 0:
            self.c[col][0] = player
            self.c[col][1] += 1
            if self.c[col][1] == self.n:
                self.winner = player
                return player
        else:
            self.c[col][0] = False
            
        # check diagonal 
        if row == col:
            if self.diagonal_1[0] == 0 or self.diagonal_1[0] == player:
                self.diagonal_1[0] = player
                self.diagonal_1[1] += 1
                if self.diagonal_1[1] == self.n:
                    self.winner = player
                    return player
                
        if row == (self.n -1 - col):
            if self.diagonal_2[0] == 0 or self.diagonal_2[0] == player:
                self.diagonal_2[0] = player
                self.diagonal_2[1] += 1
                if self.diagonal_2[1] == self.n:
                    self.winner = player
                    return player
        return 0



class TicTacToe_2:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        # 生成一个n*n的空板，0表示没有放子
        self.board = [[0] * n for j in range(n) ]
        self.size = n
        self.winner = None

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        题目说了每次输入的row和col都是唯一的，也就是，move必然是合法的
        """
        if self.winner:
            return self.winner

        self.board[row][col] = player

        # check this row
        if self.board[row] == [player]* self.size:
            self.winner = player
            return player

        # check this col
        col_sum = 0
        for i in range(self.size):
            if self.board[i][col] != player:
                break
        else:
            self.winner = player
            return player
            

        # check diagenal_1
        for i in range(self.size):
            if self.board[i][i] != player:
                break
        else:
            self.winner = player
            return player
        # check diagenal_2
        for i in range(self.size):
            if self.board[i][self.size-1-i] != player:
                break
        else:
            self.winner = player
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)