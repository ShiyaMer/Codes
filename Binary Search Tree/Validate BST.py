class Solution:
    #range need to seen
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root,up,low):
            if not root:
                return True
            if root.val>=up or root.val<=low:
                return False
            if helper(root.left,root.val,low) and  helper(root.right,up,root.val):
                return True
            return False
        return helper(root,float('inf'),-float('inf')) 
