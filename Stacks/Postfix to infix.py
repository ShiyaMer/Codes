#evaluate postfix now
#if alnum append to stack
#if operator pop first 2 elements put operator in between,put  bracket and append again
#in the end return top of the stack
class Solution:
    def postToInfix(self, postfix):
        stack=[]
        for i in postfix:
            if i.isalnum():
                stack.append(i)
            else:
                exp1=stack.pop()
                exp2=stack.pop()
                exp='('+exp2+i+exp1+')'
                stack.append(exp)
        if stack:
            return stack[-1]
