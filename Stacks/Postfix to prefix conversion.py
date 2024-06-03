#traverse
#push alnum in stack
#when operator pop 2 :append opeartor second+first
class Solution:
    def postToPre(self, post_exp):
        stack=[]
        st=""
        for i in post_exp:
            if i.isalnum():
                stack.append(i)
            else:
                j=stack.pop()
                k=stack.pop()
                stack.append(i+k+j)
        if stack:
            return stack[-1]
