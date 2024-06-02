#Initial Solution
#only one parse from left to right
#is alphabet or number put in solution
#if opening bracket push
#if closing bracket pop till opening bracket reached and pop that too
#if top of stack is higher precendence or equal precedence pop till stack empty or initial bracket reached then push lower
#if higher precendence operartor comes push
#end of expression pop stack and append all
class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        def highprecedence(topstack,y):
            if topstack==y:
                return True
            if topstack=="^":
                return True
            if topstack=='*' or topstack=='/':
                if y=='+' or y=='-':
                    return True
            if topstack=='-' and y=='+' or    (topstack=='+' and y=='-'):
                return True
            if topstack=='*' and y=='/' or    (topstack=='/' and y=='*'):
                return True    
            return False        
        stack=[]
        ans=""
        for i in exp:
            #print(i+":")
            #print(stack)
            
            if i.isalpha() or i.isnumeric():
                ans+=i
            elif len(stack)==0:
                stack.append(i)
            else:
                if i=='(':
                    stack.append(i)
                elif i==')':
                    while(len(stack)!=0 and stack[-1]!='('):
                        ans+=stack.pop()
                    if len(stack)!=0:
                        stack.pop()
                elif not highprecedence(stack[-1],i):
                    stack.append(i)
                else:
                    while(len(stack) and stack[-1]!='('):
                        ans+=stack.pop()
                    stack.append(i) 
                    
        while len(stack):
            ans+=stack.pop()
        return ans   
#Cleaner solution


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        def precedence(x):
            if x in {'-','+'}:
                return 1
            if x in {'*','/'}:
                return 2
            if x =='^':
                return 3
        def highprecedence(top,q):
            return precedence(top)>=precedence(q)
                    
        stack=[]
        ans=""
        for i in exp:
            if i.isalnum():
                ans+=i
            elif i=='(':
                stack.append(i)
            elif i==')':
                while(len(stack)!=0 and stack[-1]!='('):
                        ans+=stack.pop()
                stack.pop()
            else:
                while(len(stack) and stack[-1]!='(' and highprecedence(stack[-1],i)):
                    ans+=stack.pop()
                stack.append(i)
        while len(stack):
            ans+=stack.pop()
        return ans            
