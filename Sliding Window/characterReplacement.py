Brute:
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxi=0
        for i in range(len(s)):
            d={}
            max_frq=0
            for j in range(i,len(s)):
                d[s[j]]=d.get(s[j],0)+1
                max_frq=max(max_frq,d[s[j]])
                num_changes=(j-i+1)-max_frq 
                if num_changes<=k:
                    maxi=max(j-i+1,maxi)
                else:
                    break    
        return maxi          

                    
        

optimal:
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #max_frq=max(max_frq,d[s[j]]) at any point the minimum changes we can make
        maxi=0
        i=0
        d={}
        max_frq=0
        for j in range(len(s)):
            d[s[j]]=d.get(s[j],0)+1
            max_frq=max(max_frq,d[s[j]])#as i am always on lookout for the maximum  hence i dont update,If it updates on own fine 
            num_changes=(j-i+1)-max_frq
            """if num_changes>k:
                d[s[i]]-=1
                l=0
                for b,m in d.items():
                    if m>l:
                        l=m    
                max_frq=l """ #this is uncessary as we can let the max_freq remain as is as we need the largest change,it something bettercomes will happen automatically
                i+=1   
                         
            maxi=max(j-i+1,maxi)     
        return maxi          

                    
        
