# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        l=[]
        stack=[]
        node=root
        while(1):
            if node:
                stack.append(node)
                node=node.left
            else:
                if not stack:
                    break
                n=stack.pop()
                l.append(n.val)
                node=n.right       
        return l        
        
