Brute:
def isPowerOfTwo(n:int) -> bool:
    count=0
    for i in range(1,32):
        if n&(1<<i):
            count+=1     
    if count==1:
        return True
    return False            
Optimal:
def isPowerOfTwo(n:int) -> bool:
   return n&(n-1)==0
