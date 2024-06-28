class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        arr=[]
        stack=[root]
        while(1):
            if root.left:
                stack.append(root.left)
                root=root.left
            else:
                if len(stack)==0:
                    break    
                node=stack.pop()
                arr.append(node.val)
                if node.right:
                    stack.append(node.right)
                    root=node.right     
        i=0
        j=len(arr)-1
     
        while(i<j):
            if arr[i]+arr[j]==k:
                return True
            elif arr[i]+arr[j]<k:
                i+=1
            else:
                j-=1
        return False  
Optimal:Space ==o(h)
class BSTiterator:
    def __init__(self,root,before):
        self.root=root
        self.before=before
        self.stack=[]
        cur=root
        while(cur):
            self.stack.append(cur)
            if before:
                cur=cur.right
            else:
                cur=cur.left
    def Next(self):
        if not self.stack:
            return None
        ans=self.stack.pop()    
        if not self.before:
            if ans.right:
                curr=ans.right
                while(curr):
                    self.stack.append(curr)
                    curr=curr.left
        else:
            if ans.left:
                curr=ans.left
                while(curr):
                    self.stack.append(curr)
                    curr=curr.right
        return ans            


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        left=BSTiterator(root,False)
        right=BSTiterator(root,True)
        i,j=left.Next(),right.Next()
        while(True):
            if not i or not j or i==j:
                break
            if i.val+j.val==k:
                return True
            elif i.val+j.val<k:
                i=left.Next()
            else:
                j=right.Next()
        return False            
