class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def isvalidmove(i,j,num,board):
            for k in range(9):
                if board[i][k]==str(num):
                    return False
                if board[k][j]==str(num):
                    return False
                if board[3*(i/3)+k/3][3*(j/3)+k%3]==str(num):
                    return False
            return True        
                        
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        for k in range(1,10):
                            if isvalidmove(i,j,k,board):
                                board[i][j]=str(k)
                                if solve(board):
                                    return True
                                else:
                                    board[i][j]='.'
                        return False  #no number was being filled go back              
            return True#since everything was filled up                   

        solve(board)

        
        
