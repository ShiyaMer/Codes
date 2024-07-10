class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t) or not s or not t:
            return ""
        mini=2**31
        st=""
        i=0
        j=0
        d={}
        count=0
        for k in t:
            d[k]=d.get(k,0)+1
        count=len(d)
        while(j<len(s)):
            if s[j] in d:
                d[s[j]]-=1
                if d[s[j]]==0:
                    count-=1
            if count==0:
                while (( s[i] in d and d[s[i]]<0) or (s[i] not in d)):# it may be in negative and it we need the minimum window
                    if s[i] in d and (d[s[i]]<0):
                        d[s[i]]+=1
                    i+=1    
                if j-i+1<mini:
                    mini=j-i+1
                    st=s[i:j+1]    
                if s[i] in d:#we need to update count not above as we were incrementing i to the extra letter we encountered.
                    d[s[i]]+=1
                    if d[s[i]]>0:
                        count+=1   
                    i+=1     
            j+=1           
        return st                      

        
