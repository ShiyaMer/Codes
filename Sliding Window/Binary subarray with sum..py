class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(g):
            ans=0
            sum1=0
            i=0
            j=0
            while(j<len(nums)):
                sum1+=nums[j]
                while(sum1>g and i<=j):
                    sum1-=nums[i]
                    i+=1
                ans+=(j-i+1)
                j+=1
            return ans     
        return helper(goal)-helper(goal-1)                   
