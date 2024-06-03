#Reverse
#infix to postfix
#reverse
def infix_to_prefix(exp):
  exp=exp[::-1]
  def InfixtoPostfix(exp):
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
    ex=InfixtoPostfix(exp)
    return ex[::-1]
  
