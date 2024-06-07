class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #(difference of maximum of subarray)-(differnce of minimum of subarray)
        #for minimum same as
        #INITIALIZE LEFT WITH -1 AND RIGHT WITH LEN(ARR)
        #find the left smallest element for every elemnt 
        #find right smallest elment for every elemnt
        #ans=sum(element*(rightindex -indexof elemnt)*(leftindex-indexofelemet))
         
        n=len(nums)
        def minimum(nums,n):
            stack=[]
            left=[-1]*n
            right=[n]*n
            for i in range(n):
                if stack and nums[stack[-1]]<nums[i]:
                    stack.append(i)
                else:
                    while(stack and nums[stack[-1]]>=nums[i]):
                        ins=stack.pop()
                        if stack:
                            left[ins]=stack[-1] 
                    stack.append(i)        

            while(stack):
                ins=stack.pop()
                if stack:
                    left[ins]=stack[-1]    
            for i in range(n-1,-1,-1):
                if stack and nums[stack[-1]]<nums[i]:
                    stack.append(i)
                else:
                    while(stack and nums[stack[-1]]>nums[i]):
                        ins=stack.pop()
                        if stack:
                            right[ins]=stack[-1] 
                    stack.append(i)        
            while(stack):
                ins=stack.pop()
                if stack:
                    right[ins]=stack[-1]     
            ans=0
            for i in range(n):
                ans+=nums[i]*(i-left[i])*(right[i]-i)
            return ans   
        def maximum(nums,n):
            left=[-1]*n
            right=[n]*n
            stack=[]
            for i in range(n):
                if stack and nums[stack[-1]]>nums[i]:
                    stack.append(i)
                else:
                    while(stack and nums[stack[-1]]<=nums[i]):
                        ins=stack.pop()
                        if stack:
                            left[ins]=stack[-1] 
                    stack.append(i)        

            while(stack):
                ins=stack.pop()
                if stack:
                    left[ins]=stack[-1]    
            for i in range(n-1,-1,-1):
                if stack and nums[stack[-1]]>nums[i]:
                    stack.append(i)
                else:
                    while(stack and nums[stack[-1]]<nums[i]):
                        ins=stack.pop()
                        if stack:
                            right[ins]=stack[-1] 
                    stack.append(i)        
            while(stack):
                ins=stack.pop()
                if stack:
                    right[ins]=stack[-1]     
            ans=0
            print(left)
            print(right)
            for i in range(n):
                ans+=nums[i]*(i-left[i])*(right[i]-i)
            return ans  
        return maximum(nums,n)-minimum(nums,n)                     
