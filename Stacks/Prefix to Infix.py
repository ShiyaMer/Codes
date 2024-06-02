#reverse expression
#evaluate postfix now
#if alnum append to stack
#if operator pop first 2 elements put operator in between,put  bracket and append again
#in the end return top of the stack
class Solution:
    def preToInfix(self, pre_exp):
        stack=[]
        post=pre_exp[::-1]
        for i in post:
            if i.isalnum():
                stack.append(i)
            else:
                exp='('+stack.pop()
                exp+=i
                exp+=stack.pop()
                exp+=')'
                stack.append(exp)
        if stack:
            return stack[-1]
