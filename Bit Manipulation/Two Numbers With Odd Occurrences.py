from typing import *

def twoOddNum(arr : List[int]) -> List[int]:
    l=[]
    ans=arr[0]
    for i in range(1,len(arr)):
        ans=ans^arr[i]
    a=(ans&(ans-1))^ans#to find righmost set bit as the two numbers would differ by that
    b=0
    c=0
    for i in arr:
        if i& a:
            b=b^i
        else:
            c=c^i    
    l=[c,b]  
    l.sort(reverse=True) 
    return l    
