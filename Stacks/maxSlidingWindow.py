class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Monotonic queue solution
        ans=[]
        q=collections.deque()
        for i in range(len(nums)):
            while q and nums[i]>nums[q[-1]]:
                q.pop()
            q.append(i) 
            if q and q[0]==i-k:# ineed to remove item not coming in window ex: [1,-1] k1
                q.popleft()
            if i>=k-1:#try drawing windows 
                ans.append(nums[q[0]])  
        return ans         
        
