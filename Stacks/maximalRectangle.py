class Solution(object):
    def largestRectangleArea(self, h,maxi):
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
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        maxi=-float('inf')
        arr=[0]*len(matrix[0])
        #calculating histogram
        #since we need consecutive ones only consider if current one is 1 add on
        #else if zero set to zero
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j])==0:
                    arr[j]=0
                else:
                    arr[j]+=1
            maxi=max(self.largestRectangleArea(arr,maxi),maxi)
        return maxi            

        
