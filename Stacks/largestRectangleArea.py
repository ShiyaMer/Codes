class Solution(object):
    def largestRectangleArea(self, h):
        """
        :type heights: List[int]
        :rtype: int
        """
        #fine left border and right border then find area accordingly
        stack=[]
        maxi=-float('inf')
        right=[0]*len(h)
        for i in range(len(h)):
            if not stack:
                stack.append(i)
            elif stack and h[stack[-1]]<=h[i]:
                stack.append(i)
            elif stack:
                ind=stack.pop()
                right[ind]=ind
                while(stack and h[stack[-1]]>h[i]):
                    k=stack.pop()
                    right[k]=ind
                stack.append(i) 
        if stack:
            ind=stack.pop()
            right[ind]=ind
            while(stack):
                k=stack.pop() 
                right[k]=ind       
        left=[0]*len(h) 
        for i in range(len(h)-1,-1,-1):
            if not stack:
                stack.append(i)
            elif stack and h[stack[-1]]<=h[i]:
                stack.append(i)
            elif stack:
                ind=stack.pop()
                left[ind]=ind
                while(stack and h[stack[-1]]>h[i]):
                    k=stack.pop()
                    left[k]=ind
                stack.append(i)
        if stack:
            ind=stack.pop()
            left[ind]=ind        
            while(stack):
                k=stack.pop()
                left[k]=ind           
        print(left)
        print(right)        
        for i in range(len(h)):
            maxi=max(h[i]*(right[i]-left[i]+1),maxi) 
        return maxi                 

                       





        
