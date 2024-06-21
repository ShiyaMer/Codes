#Brute:
#Level Order travesal length and recursive solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left=0
        right=0    
        if root:
            left+=self.maxDepth(root.left)
            right+=self.maxDepth(root.right)
        return max(left,right) +1   #for current node
  #Level order travesal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q=[root]
        count=0
        while(q):
            i=len(q)
            count+=1
            for _ in range(i):
                node=q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)   
        return count             
                
#Optimal recurrence relation 1+max(left,riGht)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        return 1+max(left,right)        
                


        


