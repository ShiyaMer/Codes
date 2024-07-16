Brute:
class Solution:
    def findMatching(self, text, pattern):
        i=0
        j=0
        
        while(j<len(text)):
            if text[j]!=pattern[i]:
                j+=1
            else:
                end=j+1
                stp=i+1
                while(end<len(text) and stp<len(pattern)):
                    if text[end]==pattern[stp]:
                        end+=1
                        stp+=1
                    else:
                        break
                if stp==len(pattern):
                    return j
                else:
                    j+=1
                    
        return -1     
Optimal:
class Solution:
    def findMatching(self, text, pattern):
        i=0
        j=0
        ptlen=len(pattern)
  
        while(j<len(text)):
            if (j-i+1)<ptlen:
                j+=1
            elif (j-i+1)==ptlen:
                if text[i:j+1]==pattern:
                    return i
                else:
                    i+=1
        
        return -1                
            
