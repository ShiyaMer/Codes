class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        if n==2:
            return "11"    
        def helper(i,st):
            print(st)
            print(len(st))
            if i==(n+1):
                return st
            ans="" 
            count=1
            for j in range(1,len(st)):
                if st[j]!=st[j-1]:
                    ans+=str(count)+st[j-1]
                    count=1
                else:
                   count+=1 
            ans+=str(count)+st[-1]        
            return helper(i+1,ans)    

        st=helper(3,"11")    
        return st    

            

        
