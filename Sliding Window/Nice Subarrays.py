class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #binary subaary with sum in diffrent form
        def helper(k):
            i=0
            ans=0
            j=0
            sum1=0
            while(j<len(nums)):
                sum1+=nums[j]%2
                while sum1>k and i<=j:
                    sum1-=nums[i]%2
                    i+=1
                ans+=(j-i)+1
                j+=1  
            return ans
        return helper(k)-helper(k-1)     #at most k-at most k-1   
