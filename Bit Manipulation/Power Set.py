class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        n=len(nums)
        subsets=1<<n  #2**n
        for i in range(subsets):
            sub=[]
            for j in range(n):
                if i&(1<<j):
                    sub.append(nums[j])
            ans.append(sub)        


        return ans
