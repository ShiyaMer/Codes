class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #since bst inorder will be the order od sorted#left root right
        #morris order traversal
        cur=root
        cnt=0
        while(cur):
            if not cur.left:
                cnt+=1
                if cnt==k:
                    return cur.val
                cur=cur.right    
            else:
                pointer=cur.left
                while(pointer.right and pointer.right!=cur):
                    pointer=pointer.right
                if not pointer.right:
                    pointer.right=cur
                    cur=cur.left
                else:
                    pointer.right=None
                    cnt+=1
                    if cnt==k:
                        return cur.val
                    cur=cur.right  
        return -1              


        
