class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #find node
        #Attach right node to the right of leftmost node
        def helper(node):#the node to deleted is sent
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            pointer=node.left#i take the next left elemnt
            while(pointer.right):
                pointer=pointer.right   
            pointer.right=node.right#atttch the right part to left's right
            l=node.left#remember pointer
            node.left=node.right=None#deletion
            return l    
        if not root:
            return root
        if root.val==key:
            root=helper(root)
        else:
            cur=root
            while(cur):
                if cur.val>key:
                    if cur.left and cur.left.val==key:#i need to send one node above that one
                        cur.left=helper(cur.left)
                        break
                    else:
                        cur=cur.left    
                else:
                    if cur.right and cur.right.val==key:
                        cur.right=helper(cur.right)
                        break
                    else:
                        cur=cur.right
        return root
              
