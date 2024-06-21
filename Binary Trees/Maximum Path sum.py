# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def maxi(root,mi):
            if not root:
                return 0
            lh=max(0,maxi(root.left,mi))#no the consider negative values
            rh=max(0,maxi(root.right,mi))
            mi[0]=max(mi[0],root.val+lh+rh)
            return root.val+max(lh,rh)#this accounts for negative +positive=posituive 
        mi=[-2**31]
        maxi(root,mi)
        return mi[0]

        
