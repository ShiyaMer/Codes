class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #opposite of preorder traversal
        post=[]
        cur=root
        while(cur):
            if not cur.right:
                post.append(cur.val)
                cur=cur.left
            else:
                prev=cur.right
                while(prev.left and prev.left!=cur):
                    prev=prev.left
                if not prev.left:
                    prev.left=cur
                    post.append(cur.val) #root,left,right
                    cur=cur.right
                else:
                    prev.left=None
                    cur=cur.left
        return post[::-1]                            
        
