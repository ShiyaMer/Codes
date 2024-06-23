# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        maxi=0    
        pow=0
        q=[[root,0]]
        level=[]
        while(q):
            l=[]
            j=len(q)
            for _ in range(j):
                node=q.pop(0)
                l.append(node[1])
                if node[0].left:
                    q.append([node[0].left,2*node[1]+1])
                if node[0].right:
                    q.append([node[0].right,2*node[1]+2])
 
            maxi=max(l[-1]-l[0]+1,maxi)
        return maxi    


        
