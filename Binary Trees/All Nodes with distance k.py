# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Find parents to enable backward travesal
#Move radially from target increasing the distance each time
class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return []
        if k==0:
            return [target.val]    
        q0=[root]
        d={root:None}
        while(q0):
            i=len(q0)
            for _ in range(i):
                n=q0.pop(0)
                if n.left:
                    d[n.left]=n
                    q0.append(n.left)
                if n.right:
                    d[n.right]=n
                    q0.append(n.right)
        visited=[]
        q=[target]
        dis=0
        while(q):
            i=len(q)
            l=[]
            for _ in range(i):
                n=q.pop(0)
                if n not in visited:
                    visited.append(n)
                if d[n] and d[n] not in visited:
                    q.append(d[n])
                    visited.append(d[n])
                if n.left and n.left not in visited:
                    q.append(n.left)
                    visited.append(n.left)
                if n.right and n.right not in visited:
                    q.append(n.right)
                    visited.append(n.right)
            dis+=1
            if dis==k:
                break    
        ans=[]   
        for i in q:
            ans.append(i.val)
        return ans  







        
