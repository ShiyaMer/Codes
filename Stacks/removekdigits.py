class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        ## IDEA : 1234, k= 2 => when numbers are in increasing order we need to delete last digits 
        ## 4321 , k = 2 ==> when numbers are in decreasing order, we need to delete first digits
        ## so, we need to preserve increasing sequence and remove decreasing sequence ##
		## LOGIC ##
		#	1. First think in terms of stack
		#	2. push num into stack IF num it is greater than top of stack
        stack=[]
        for i in num:
            if stack and stack[-1]<i:
                stack.append(i)
            else:
                while(stack and stack[-1]>i and k!=0):
                    stack.pop()
                    k-=1
                stack.append(i)
        while(k):
            stack.pop()
            k-=1        
        if not stack:
            return "0"
        ans= "".join(stack)  
        return str(int(ans))  




        
