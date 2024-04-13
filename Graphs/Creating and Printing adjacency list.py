from typing import List, Tuple

def printAdjacency(n: int, m: int, edges: List[Tuple[int, int]]) -> List[List[int]]:
    d={}
    for i in range(n):
        d[i]=[i]
    for x,y in edges:
        d[x].append(y)
        d[y].append(x)  
    ans=[]    
    for  i,j in d.items():
        ans.append(j)
    return ans    


