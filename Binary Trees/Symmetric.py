# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def help(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return help(p.left,q.right) and help(p.right,q.left)    
        if not root:
            return True
        return help(root.left,root.right)        
#Iterative:
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q=[[root.left,root.right]]
        while(q):
            n=q.pop(0)
            left=n[0]
            right=n[1]
            if not left and not right:
                continue
            elif not left or not right:
                return False
            else:
                if (left.val)!=(right.val):
                    return False
                else:
                    q.append([left.left,right.right])
                    q.append([left.right,right.left])       
        return True                 
