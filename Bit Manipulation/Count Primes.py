brute:
def countPrimes(n: int) -> int:
    count=[]
    def check(k):
        for i in range(2,int(k**0.5)+1):
            if k%i==0:
                return False
        return True        
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if check(i):
                count.append(i)
                #print(i)
            if n//i!=i and check(n//i):
                count.append(n//i)    
    return count            

optimal:
def countPrimes(n: int) -> int:
    count=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            count.append(i)
            while(n%i==0):
                n=n//i
    if n!=1:
        count.append(n)            
               
    return count
    Further Optimal:Sieve of Erasthones
    def countPrimes(n: int) -> int:
    pr=[1]*(n+1)
    pr[0]=0
    pr[1]=0
    l=[]
    for i in range(2,n):
       if pr[i]==1:
            if n%i==0:
               l.append(i)
            for j in range(i*i,n,i):
                pr[j]=0
    return   l       
