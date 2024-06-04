class Solution(object):
    def nextGreaterElements(self, nums):
    #play with indexes    
    #start from end element in  array
    #put element in stack
    #if element is  strictly smaller than element in stack push
    #else pop and assign the top of stack element to the nextgreaterelemnt of the popped elent
    #repeat above step till the elemnt is smaller than top of stack or stack empty
    #push elemnt 
    #Traverse the arrya again for circular elements
    #and do the same steps
    #in the end traverse through stack to assign neighbors
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[-1]*len(nums)
        stack=[]
        n=len(nums)
        for i in range(n-1,-1,-1):
            if stack and nums[i]<nums[stack[-1]]:
                stack.append(i)
            else:
                while(stack and nums[i]>=nums[stack[-1]]):
                    ind=stack.pop()
                    if stack:
                        ans[ind]=nums[stack[-1]]
                stack.append(i)  
        for i in range(n-1,-1,-1):
            if stack and nums[i]<nums[stack[-1]]:
                stack.append(i)
            else:
                while(stack and nums[i]>=nums[stack[-1]]):
                    ind=stack.pop()
                    if stack:
                        ans[ind]=nums[stack[-1]]  
                stack.append(i)
        while(stack):
            ind=stack.pop()
            if stack:
                ans[ind]=nums[stack[-1]]
        return ans                

        
