class Solution:
    def subarraysWithKDistinct(self, s: List[int], k: int) -> int:
        def helper(k):
            d={}
            i=0
            j=0
            ans=0
            while(j<len(s)):
                d[s[j]]=d.get(s[j],0)+1
                while len(d)>k and i<=j:
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        del d[s[i]]
                    i+=1
      
                ans+=(j-i+1)  
                j+=1
            return ans
        return helper(k)-helper(k-1)    
        
