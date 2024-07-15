Brute:
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in s:
            if (stack) and (stack[-1]=='(' and i==')'):
                stack.pop()
                continue
            else:
                stack.append(i)
        return len(stack)            

  Optimal:
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open=0
        close=0
        for i in s:
            if i=="(":
                open+=1
            elif open==0:
                close+=1
            else:
                open-=1
        return open+close                           

        
