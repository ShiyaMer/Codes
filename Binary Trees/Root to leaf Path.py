
class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        def help(node,ans,path):
            if not node.left and not node.right:
                ans.append(path)
                return
            if node.left:
                help(node.left,ans,path+[node.left.data]) 
            if node.right:
                help(node.right,ans,path+[node.right.data]) 
        help(root,ans,[root.data])
        return ans
