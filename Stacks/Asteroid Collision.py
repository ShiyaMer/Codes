class Solution(object):
    def asteroidCollision(self, asteroids):
        #[-2,-1,1,2] ans=[-2,-1,1,2]
        #case of pop is only when top of stack id positive and asteroid is negative
        #we are given that asteriod will never bw zero
        
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for i in asteroids:
            while(stack and stack[-1]>0 and i<0):
                diff=stack[-1]+i
                if diff<0:
                    stack.pop()
                elif diff>0:
                    i=0
                else:
                    i=0
                    stack.pop()
            if i!=0:
                stack.append(i)                
  
        ans=[]
        while(stack):
            ans.append(stack.pop()) 
        ans=ans[::-1]   
        return ans                     
        
