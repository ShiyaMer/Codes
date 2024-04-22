Brute:
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi=0
        j=0
        for i in range(len(nums)):
            c=0
            for j in range(i,len(nums)):
                if nums[j]==0:
                    c+=1
                if c<=k:
                    maxi=max(maxi,j-i+1)
                    #print("maxi"+str(maxi)+" "+"j"+str(j)+"i"+str(i))
    
                else:
                    break    
        return maxi                
                   
        Better:
      class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi,i,j,zero=0,0,0,0
        while(j<len(nums)):
            print(zero)
            if nums[j]==0:
                zero=zero+1
            while(zero>k):#is not  the most optimal as the while adds to complexity within
                if nums[i]==0:
                    zero=zero-1
                i=i+1    
            if zero<=k:
                maxi=max(maxi,j-i+1)
                  
            j+=1
     
        return maxi                
                   
        
      Optimal:
      class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi,i,j,zero=0,0,0,0
        while(j<len(nums)):
            print(zero)
            if nums[j]==0:
                zero=zero+1
            if(zero>k):#if the most optimal as the window not allowed to move so the while eliminated till zeros does not become less than k maxi not updated
                if nums[i]==0:
                    zero=zero-1
                i=i+1    
            if zero<=k:
                maxi=max(maxi,j-i+1)
                  
            j+=1
     
        return maxi                
                   
        
