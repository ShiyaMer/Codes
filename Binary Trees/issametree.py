class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False    
        if p.val!=q.val:
            return False
        l=self.isSameTree(p.left,q.left)
        r=self.isSameTree(p.right,q.right)
        return l and r   

