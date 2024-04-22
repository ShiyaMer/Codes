Brute:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s)==1:
            return 1
        maxi=0
        for i in range(len(s)):
            d={}  
            count=0
            for j in range(i,len(s)):
                if s[j] not in d:
                    d[s[j]]=1
                    count=count+1
                    print(count)
                else: 
                    print(d)
                    maxi=max(count,maxi)
                    count=0
                    break
            maxi=max(count,maxi)            
        return maxi             


Optimal:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s)==1:
            return 1
        maxi=0
        d={}
        i=0
        j=0
        while(j<len(s)):
            if s[j] in d and d[s[j]]>=i:#tmmzuxt so i avois the case when i reach t again in the end i doesnt revert back
                i=d[s[j]]+1
                d[s[j]]=j
            else:
                d[s[j]]=j     
                maxi=max(j-i+1,maxi)        
            j+=1 
            print(maxi)
               
        #maxi=max(j-i+1,maxi)      
        return maxi                     



        
