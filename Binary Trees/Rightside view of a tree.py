class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        q=[[root,0]] 
        ans=[]
        while(q):
            i=len(q)
            for _ in range(i):
                n=q.pop(0)
                node=n[0]
                level=n[1]
                if len(ans)<=level:
                    ans.append(node.val)
                else:
                    ans[level]=node.val    
                if node.left:
                    q.append([node.left,level+1])
                if node.right:
                    q.append([node.right,level+1]) 
        return ans                   


        
