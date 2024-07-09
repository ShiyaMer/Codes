def numberOfSubstrings(self, s: str) -> int:
        d={}
        i=0
        j=0
        ans=0
        while(j<len(s)):
            d[s[j]]=d.get(s[j],0)+1
            print(d)
            while len(d)==3 and i<=j:
                ans+=len(s)-j#it can form subarrys till end of string
                d[s[i]]-=1
                if d[s[i]]==0:
                    del d[s[i]]
                i+=1 
                
            j+=1

        return ans
        
