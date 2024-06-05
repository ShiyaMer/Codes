class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        stack=[]
        ans=[-1]*len(A)
        n=len(A)
        for i in range(n):
            if stack and A[i]>A[stack[-1]]:
                stack.append(i)
            else:
                while(stack and A[i]<=A[stack[-1]]):
                    ind=stack.pop()
                    if stack:
                        ans[ind]=A[stack[-1]]
                stack.append(i)
        while(stack):
            ind=stack.pop()
            if stack:
                ans[ind]=A[stack[-1]]
                    
        return ans        
