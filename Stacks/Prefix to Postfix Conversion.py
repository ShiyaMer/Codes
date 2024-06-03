Brute force:
#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        def pretoinfix(exp):
            exp=exp[::-1]
            stack=[]
            for i in exp:
                if i.isalnum():
                    stack.append(i)
                else:
                    j=stack.pop()
                    k=stack.pop()
                    stack.append('('+j+i+k+')')
            if stack:
                return stack[-1]
        def inftopost(exp):
            stack=[]
            st=""
            def precendence(x):
                if x in {'+','-'}:
                    return 1
                if x in {'*','/'}:
                    return 2
                if x=='^':
                    return 3
            def highprecendence(top,y):
                if precendence(top)>=precendence(y):
                    return True
            for i in exp:
                if i.isalnum():
                    st+=i
                elif i=='(':
                    stack.append(i)
                elif i==')':
                    while(len(stack) and stack[-1]!='('):
                        st+=stack.pop()
                    stack.pop()
                else:
                    while(len(stack) and stack[-1]!='(' and highprecendence(stack[-1],i)):
                        st+=stack.pop()
                    stack.append(i)
            return st
        return (inftopost(pretoinfix(pre_exp)))        
                    

Optimal:
#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        exp=pre_exp[::-1]
        stack=[]
        for i in exp:
            if i.isalnum():
                stack.append(i)
            else:
                j=stack.pop()
                k=stack.pop()
                stack.append(j+k+i)
        if stack:
            return stack[-1]
        
                    
        # Code here
