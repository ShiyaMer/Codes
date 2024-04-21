Brute:
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        def prime(k):
            
            for i in range(2,int(k**0.5)+1):
                if k%i==0:
                    return False
            return True    
        for i in range(2,n):
            
            if prime(i):
                print(i)
                count+=1
        return count 
optimal:
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
        count=0
        arr=[1]*(n+1)
        arr[0]=0
        arr[1]=0
        arr[n]=0
        for i in range(2,n):
            if arr[i]==1:
                for j in range(i*i,n,i):
                    arr[j]=0

        return sum(arr)     
