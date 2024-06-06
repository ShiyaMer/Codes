#Brute:
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def find(ind,height,left,right):
            if left:
                stack=[]
                for i in range(ind-1,-1,-1):
                    if stack and stack[-1]<height[i]:
                        stack.append(height[i])
                    elif not stack:
                        stack.append(height[i])
                if stack:
                    return stack[-1]
                else:
                    return 0             
            elif right:
                stack=[]
                for i in range(ind+1,len(height)):
                    if stack and stack[-1]<height[i]:
                        stack.append(height[i])
                    elif not stack:
                        stack.append(height[i])
                if stack:
                    return stack[-1]
                else:
                    return 0                      
        count=0
        for i in range(len(height)):
            l=find(i,height,True,False)
            r=find(i,height,False,True)
            ans=min(l,r)-height[i]
            if ans>0:
                count+=ans
        return count    

        
#Better:
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        right=[0]*len(height)
        left=[0]*len(height)
        mini=0
        for i in range(1,len(height)):
            if height[i-1]>mini:
                mini=height[i-1]
            left[i]=mini 
        mini=0    
        for i in range(len(height)-2,-1,-1):
            if height[i+1]>mini:
                mini=height[i+1]
            right[i]=mini         
        count=0
        for i in range(len(height)):
            l=left[i]
            r=right[i]
            ans=min(l,r)-height[i]
            if ans>0:
                count+=ans
        return count    
#Optimal:
#two pointer left=0 and right=index of array -1
#leftmax and rightmax
#we check only whether leftmax<=rightmax as it will the minimum border under consideration
#update leftmax and rightmax if current elemnt is greater
#move pointer
#stopping when one pointer crosses the othe
class Solution(object):
    def trap(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        count=0
        l=0
        r=len(h)-1
        leftmax=h[l]
        rightmax=h[r]
        while(l<=r):
            if leftmax<=rightmax:
                if leftmax-h[l]>0:
                    count+=leftmax-h[l]
                if h[l]>leftmax:
                    leftmax=h[l]  
                l+=1    
            else:
                print(rightmax)
                if rightmax-h[r]>0:
                    count+=rightmax-h[r]
                if h[r]>rightmax:
                    rightmax=h[r]
                r-=1    
        return count  

