#Brute:
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count=0
        n=len(arr)
        for i in range(n):
            for j in range(i,n):
                count+=min(arr[i:j+1])
        return count%(10**9 + 7 )
#Optimal:
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        #INITIALIZE LEFT WITH -1 AND RIGHT WITH LEN(ARR)
        #find the left smallest element for every elemnt 
        #find right smallest elment for every elemnt
        #ans=sum(element*(rightindex -indexof elemnt)*(leftindex-indexofelemet))
        n=len(arr)
        right=[n]*n
        left=[-1]*n#this means no samller elemnt to left all are greater if it is the staring position then the value should be one
        stack=[]
        for i in range(n):
            if stack and arr[i]>arr[stack[-1]]:
                stack.append(i)
            else:
                while(stack and arr[i]<=arr[stack[-1]]):
                    ind=stack.pop()
                    if stack:
                        left[ind]=stack[-1]
                stack.append(i)
        while(stack):
            ind=stack.pop()
            if stack:
                left[ind]=stack[-1]
        for i in range(n-1,-1,-1):
            if stack and arr[i]>arr[stack[-1]]:
                stack.append(i)
            else:
                while(stack and arr[i]<arr[stack[-1]]):
                    ind=stack.pop()
                    if stack:
                        right[ind]=stack[-1]
                stack.append(i)
        while(stack):
            ind=stack.pop()
            if stack:
                right[ind]=stack[-1]
        ans=0
        print(left)
        print(right)
        for i in range(n):
            l=left[i]
            r=right[i] 
            ans+=(arr[i]*(i-l)*(r-i) )
        return ans%(10**9 + 7)   

