class Solution:
    def minWindow(self, s,t):
        if len(s)<len(str2) or not s or not t:
            return ""
        
        i=0
        j=0
        mini=2**31
        ans=""
        while(j<len(s)):
            if s[j]==t[0]:
                start=j
                end=j+1
                t_trav=1
                while(t_trav<len(t) and end<len(s)):
                    if s[end]==t[t_trav]:
                        t_trav+=1
                    end+=1
                end=end-1
                if  t_trav==len(t) and (end-start+1)<mini:
                    mini=end-start+1
                    ans=s[start:end+1]
            j+=1
        return ans    
