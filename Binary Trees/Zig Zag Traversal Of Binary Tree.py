# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q=[root]
        ans=[]
        k=True
        while(q):
            l=[]
            i=len(q)
            for _ in range(i):
                node=q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                l.append(node.val)   
            
            if k==True:
                ans.append(l)
            else:
                l=l[::-1]
                ans.append(l)
            k=not k    
        return ans        


        
