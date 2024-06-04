class Solution(object):
    #start from end element in bigger array
    #put element in stack
    #if element is smaller than elemnt in stack push
    #else pop and assign the top of stack element to the nextgreaterelemnt of the popped elent
    #repeat above step till the elemnt is smaller than top of stack or stack empty
    #push elemnt 
    #the traverse smaller array to assign nextgreaterelemnt from the dictionary created.

    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[-1]*len(nums1)
        n=len(nums2)
        d={}
        stack=[]
        for i in range(len(nums2)-1,-1,-1):
            if stack and nums2[i]<stack[-1]:
                stack.append(nums2[i])
            else:
                while(stack and stack[-1]<nums2[i]):
                    ele=stack.pop()
                    if stack:
                        d[ele]=stack[-1]
                    else:
                        d[ele]=-1
                stack.append(nums2[i])
        while(stack):
            ele=stack.pop()
            if stack:
                d[ele]=stack[-1]
            else:
                d[ele]=-1
        for i in range(len(nums1)):
            ans[i]=d[nums1[i]]   

        return ans         




        
