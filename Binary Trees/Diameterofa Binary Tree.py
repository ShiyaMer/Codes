class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def maxi(root,ans):
            if not root:
                return 0
            lh=maxi(root.left,ans)
            rh=maxi(root.right,ans) 
            ans[0]=max(ans[0],lh+rh)
            return 1+ max(lh,rh)
        ans=[0]  
        maxi(root,ans)
        return ans[0]


        
