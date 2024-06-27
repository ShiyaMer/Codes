class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
     
        if not root or root==p or root==q:
            return root
        if (p.val<root.val and root.val<q.val) or (p.val>root.val and root.val>q.val):
            return root
        elif p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p, q) 
        elif p.val<root.val and q.val<root.val:
             return self.lowestCommonAncestor(root.left, p, q)
