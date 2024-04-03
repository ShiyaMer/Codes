from typing import *

def graphColoring(mat: List[List[int]], m: int) -> str:
    n=len(mat)
    color=[0]*n
    def issafe(node,mat,color,m,n,assn):
        for i in range(n):
            if mat[node][i]==1 and color[i]==assn:
                return False
        return True        
    def helper(node,mat,color,m,n):
        if  node==n:
            return True
        for i in range(1,m+1):
            if issafe(node,mat,color,m,n,i):
                color[node]=i
                if helper(node+1,mat,color,m,n):
                    return True
                else:
                    color[node]=0
        return False     
    ans= helper(0,mat,color,m,n)    
    if ans:
        return "YES"
    return "NO"                   
                
