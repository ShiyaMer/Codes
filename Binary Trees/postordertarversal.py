# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def help(root,l):
            if not root:
                return
            help(root.left,l)
            help(root.right,l)
            l.append(root.val)
        l=[]
        help(root,l)
        return l        
        
