class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur=root
        while(cur):
            if val>cur.val:
                if not cur.right:
                    cur.right=TreeNode(val)
                    break
                cur=cur.right
            else:
                if not cur.left:
                    cur.left=TreeNode(val)
                    break
                cur=cur.left
        return root        

        
