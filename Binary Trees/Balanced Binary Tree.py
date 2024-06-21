#Brute:
#Check for every node whether left height-right height<=1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def lefth(root):
            if not root:
                return 0
            lh=lefth(root.left)
            rh=lefth(root.right)
            return 1+max(lh,rh)      
        l=lefth(root.left)
        r=lefth(root.right)
        if abs(l-r)>1:
            return False
        k=self.isBalanced(root.left)
        j=self.isBalanced(root.right)
        if not k or not j:
            return False
        return True         

#Optimal
#I can add check to the maxi function

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def maxi(root):
            if not root:
                return 0
            lh=maxi(root.left)
            rh=maxi(root.right)
            if lh==-1 or rh==-1:#if any one of the child node is imbalanced i can return from there directly.
                return -1
            if abs(lh-rh)>1:
                return -1    
            return 1+max(lh,rh)      
        return maxi(root)!=-1
        
