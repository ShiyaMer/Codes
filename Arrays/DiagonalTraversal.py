class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        l=[]
        up=True
        row=0
        col=0
        while(row<len(mat) and col<len(mat[0])):
            if up:
                while(row>0 and col<len(mat[0])-1):
                    l.append(mat[row][col])
                    row-=1
                    col+=1
                l.append(mat[row][col])    
                if col==len(mat[0])-1:
                    row+=1
                else:
                    col+=1    
            else:
                while(col>0 and row<len(mat)-1):
                    l.append(mat[row][col])
                    row+=1
                    col-=1
                l.append(mat[row][col])    
                if row==len(mat)-1:
                    col+=1
                else:
                    row+=1    
            up=not(up)  
        return l          

                
        
