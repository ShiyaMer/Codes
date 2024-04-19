Brute:
def count(n):
    co=0
    for i in range(0,32):
        if n&(1<<i):
            co+=1        
    return co  

def countSetBits(N: int) -> int:
    cnt=0
    for i in range(1,N+1):
        cnt+=count(i)
    return cnt  
  #Better
def count(n):
    co=0
    while(n):
        n=n&(n-1)
        co+=1     
    return co  

def countSetBits(N: int) -> int:
    cnt=0
    for i in range(1,N+1):
        cnt+=count(i)
    return cnt    
