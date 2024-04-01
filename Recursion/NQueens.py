            
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def issafe(ro,col,board,n):
            #since i am moving up to down column by column there are only ceratin things i need to check
        #upper diangonal towards left col--,row--
        #left side col--
        #lower diagonal towards left row++ col--
            row=ro
            column=col
            while(row>=0 and column>=0):
                if board[row][column]=="Q":
                    return False
                row-=1
                column-=1

            column=col
            while(column>=0):
                if board[ro][column]=="Q":
                    return False
                column-=1
            row=ro
            column=col
            while(row< n and column>=0):
                if board[row][column]=="Q":
                    return False
                column-=1
                row+=1    
            return True

        def solve(col,ans=[],board=[["." for _ in range(n)] for _ in range(n)]):

            if col==n:
                ans.append(["".join(board[j]) for j in range(n)])
                return
            for ro in range(n):
                if issafe(ro,col,board,n):
                    board[ro][col]="Q"
                    solve(col+1,ans,board)
                    board[ro][col]="."  
            return ans         

         
        return solve(0)
        
